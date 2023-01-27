from pydantic import Field, BaseSettings
from typing import Optional


class TopicSchema(BaseSettings):
    TOPICS_NAME: str = Field(example="people.basic.python", description="topic name")
    TOPICS_PARTITIONS: Optional[int] = Field(example=3, description="topic partition")
    TOPICS_REPLICAS: Optional[int] = Field(example=3, description="topic replicas")
    RETENTION_TIME: Optional[str] = Field(example='2000', description="topic retention time")

# topic_schema = TopicSchema()
