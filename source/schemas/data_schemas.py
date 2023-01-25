from pydantic import Field, BaseSettings
from typing import Optional


class TopicSchema(BaseSettings):
    TOPICS_NAME: str = Field(example="people.basic.python", description="topic name")
    TOPICS_PARTITIONS: Optional[int] = Field(example=3, description="topic partition")
    TOPICS_REPLICAS: Optional[int] = Field(example=3, description="topic replicas")


# topic_schema = TopicSchema()
