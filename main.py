import os

from dotenv import load_dotenv
from fastapi import FastAPI
from kafka import KafkaAdminClient
from uvicorn import Server, Config

from configuration.config import server_config
from source.apis.kafka_apis import kafka_route
from source.utils.client_instance import kafka_client

# verbbose = true to get loud errors if anything goes wrong
load_dotenv(verbose=True)
app = FastAPI()
app.include_router(kafka_route)


@app.on_event('startup')
async def startup_event():
    kafka_client.kafka_client = KafkaAdminClient(bootstrap_servers=os.getenv('BOOTSTRAP_SERVERS'))


if __name__ == '__main__':
    server = Server(Config(app=app, host=server_config.HOST, port=server_config.PORT))
    server.run()
