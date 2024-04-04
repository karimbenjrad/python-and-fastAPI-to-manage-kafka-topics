## README

### Introduction
This repository contains a FastAPI application that provides endpoints to interact with Apache Kafka topics and produce messages to Kafka.

### Installation
1. Clone the repository:
   ```
   git clone https://github.com/karimbenjrad/python-and-fastAPI-to-manage-kafka-topics
   ```
2. Install the required dependencies using pip:
   ```
   pip install -r requirements.txt
   ```

### Usage
1. Run the FastAPI application by executing `main.py`:
   ```
   python main.py
   ```
   This will start the FastAPI server, and you can access the endpoints described below.

### Endpoints
- **POST /add-topic**: Add a new Kafka topic.
  - Request body: JSON object with topic details.
  - Response: Details of the added topic.
  
- **POST /alter-topic**: Alter an existing Kafka topic.
  - Request body: JSON object with topic details.
  - Response: Details of the altered topic.
  
- **GET /show-topics**: Retrieve a list of all Kafka topics.
  - Response: List of Kafka topics.
  
- **POST /produce**: Produce a message to a Kafka topic.
  - Request body: JSON object with message details.
  - Response: Confirmation message.

### Dependencies
- `fastapi`: FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.
- `kafka-python`: Kafka-python is the Python client for Apache Kafka and is implemented to be producer/consumer compatible with Kafka broker versions 0.8.x and later.

### Contributing
Contributions are welcome! Please feel free to submit a pull request with any improvements or fixes.
