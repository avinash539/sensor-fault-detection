import sys
from sensor.logger import logging
from sensor.exception import SensorException
from sensor.configuration.mongodb_connection import MongoDBClient
from sensor.pipeline.training_pipeline import TrainPipeline


def test_error():
    try:
        x = 1 / 0
    except Exception as e:
        raise SensorException(e, sys)


if __name__ == "__main__":
    train_pipeline = TrainPipeline()
    train_pipeline.run_pipeline()

