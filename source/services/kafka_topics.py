import os

from kafka import KafkaProducer
from kafka.admin import NewTopic, ConfigResource, ConfigResourceType
from kafka.errors import TopicAlreadyExistsError
from source.exceptions.producer_exceptions import ErrorHandler
from source.schemas.data_schemas import ProduceSchema
from source.schemas.data_schemas import TopicSchema
from source.utils.client_instance import kafka


class KafkaTopic:
    @staticmethod
    def add_topic(topic_schema: TopicSchema):
        topic = NewTopic(name=topic_schema.TOPICS_NAME,
                         num_partitions=topic_schema.TOPICS_PARTITIONS,
                         replication_factor=topic_schema.TOPICS_REPLICAS,
                         topic_configs={"retention.ms": topic_schema.RETENTION_TIME})
        try:
            kafka.kafka_client.create_topics([topic])
            result = "topic created ! "
        except TopicAlreadyExistsError as error:
            result = "topic already exists"
        finally:
            # kafka.kafka.close()
            return result

    @staticmethod
    def alter_topic(topic_schema: TopicSchema):
        cfg_resource_update = ConfigResource(
            ConfigResourceType.TOPIC,
            topic_schema.TOPICS_NAME,
            configs={'retention.ms': topic_schema.RETENTION_TIME,
                     "num.partitions": topic_schema.TOPICS_PARTITIONS,
                     "replication.factor": topic_schema.TOPICS_REPLICAS, }
        )
        kafka.kafka_client.alter_configs([cfg_resource_update])
        # kafka.kafka.close()

    @staticmethod
    def show_topics():
        return kafka.kafka_consumer.topics()


class KafkaProduce:
    @staticmethod
    def produce_person(producer_message: ProduceSchema):
        kafka.kafka_producer = KafkaProducer(bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'],
                                             linger_ms=producer_message.LINGER_MS,
                                             retries=producer_message.RETRIES,
                                             max_in_flight_requests_per_connection=producer_message.INFLIGHT_REQS,
                                             acks=producer_message.ACK)
        kafka.kafka_producer.send(topic=producer_message.TOPIC_NAME, key=producer_message.MESSAGE_KEY.encode('utf-8'),
                                  value=producer_message.PERSON.json().encode('utf-8')).add_errback(ErrorHandler(producer_message.PERSON))
        kafka.kafka_producer.flush()
