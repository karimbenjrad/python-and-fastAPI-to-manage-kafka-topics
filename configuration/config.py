from pydantic import BaseSettings, Field


class ServerConfig(BaseSettings):
    """
    Class for server configurations
    """
    HOST: str = Field(default="0.0.0.0", description="Host of the application", env="SERVER_HOST")
    PORT: int = Field(default=8001, description="Port of the application", env="SERVER_PORT")


class KafkaConfig(BaseSettings):
    """
    class for kafka configurations
    """
    BOOTSTRAP_SERVERS: str = Field(default="localhost:9092,localhost:9093,localhost:9094",
                                   description="bootstrap server", env="BOOTSTRAP_SERVERS")
    # TOPICS_PEOPLE_BASIC_NAME: str = Field(default="people.basic.python", description="topic name",
    #                                       env="TOPICS_PEOPLE_BASIC_NAME")
    # TOPICS_PEOPLE_BASIC_PARTITIONS: int = Field(default=3, description="topic partition",
    #                                             env="TOPICS_PEOPLE_BASIC_PARTITIONS")
    # TOPICS_PEOPLE_BASIC_REPLICAS: int = Field(default=3, description="topic replicas",
    #                                           env="TOPICS_PEOPLE_BASIC_REPLICAS")


kafka_config = KafkaConfig()
server_config = ServerConfig()
