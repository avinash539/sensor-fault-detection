import os
import pymongo
import certifi
from sensor.constant.database import DATABASE_NAME
from sensor.constant.env_variable import MONGO_URL_KEY

ca = certifi.where()


class MongoDBClient:
    client = None

    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv(MONGO_URL_KEY)
                if mongo_db_url is None:
                    raise Exception(f"Environment key: {MONGO_URL_KEY} is not set.")
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
        except Exception as e:
            raise e
