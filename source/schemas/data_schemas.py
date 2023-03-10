from pydantic import Field, BaseSettings
from typing import Optional


class TopicSchema(BaseSettings):
    TOPICS_NAME: str = Field(example="people.basic.python", description="topic name")
    TOPICS_PARTITIONS: Optional[int] = Field(example=3, description="topic partition")
    TOPICS_REPLICAS: Optional[int] = Field(example=3, description="topic replicas")
    RETENTION_TIME: Optional[str] = Field(example='2000', description="topic retention time")


class PersonSchema(BaseSettings):
    id: str = Field(example="0", description="person id")
    name: str = Field(example="karim", description="person name")
    title: str = Field(example="software data engineer", description="person function")


class ProduceSchema(BaseSettings):
    TOPIC_NAME: str = Field(example="people.basic.python", description="topic name")
    MESSAGE_KEY: str = Field(example="0", description="topic key")
    LINGER_MS: int = Field(example=600, description="batch per time")
    RETRIES: int = Field(example=5, description="how much retries to perform before failing")
    INFLIGHT_REQS: int = Field(example=1, description="control the order of the batches to be sent")
    ACK: str = Field(example="all", description="ackisition of data")
    PERSON: PersonSchema

# topic_schema = TopicSchema()
