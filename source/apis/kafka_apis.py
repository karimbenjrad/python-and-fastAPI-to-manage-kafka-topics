import logging

from fastapi import APIRouter, Depends

from source.schemas.data_schemas import TopicSchema
from source.services.kafka_topics import KafkaTopic

kafka_route = APIRouter()
logger = logging.getLogger()


@kafka_route.post('/add-topic')
async def add_topic(topic: TopicSchema, topic_service: KafkaTopic = Depends(KafkaTopic)):
    return topic_service.add_topic(topic)