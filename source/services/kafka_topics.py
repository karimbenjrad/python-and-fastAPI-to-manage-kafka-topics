from source.schemas.data_schemas import TopicSchema
import logging

from fastapi import APIRouter

from kafka.admin import NewTopic
from kafka.errors import TopicAlreadyExistsError
from source.schemas.data_schemas import TopicSchema
from source.utils.client_instance import kafka_client


class KafkaTopic:
    def add_topic(self, topic_schema: TopicSchema):
        topic = NewTopic(name=topic_schema.TOPICS_NAME,
                         num_partitions=topic_schema.TOPICS_PARTITIONS,
                         replication_factor=topic_schema.TOPICS_REPLICAS)
        try:
            kafka_client.kafka_client.create_topics([topic])
            result = "topic created ! "
        except TopicAlreadyExistsError as error:
            result = "topic already exists"
        finally:
            kafka_client.kafka_client.close()
            return result
