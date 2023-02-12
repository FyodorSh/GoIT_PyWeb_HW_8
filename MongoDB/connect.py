import configparser

from mongoengine import connect


config = configparser.ConfigParser()
config.read("config.ini")

mongo_user = config.get("DB", "user")
mongo_pass = config.get("DB", "pass")
domain = config.get("DB", "domain")
db_name = config.get("DB", "db_name")

connect(host=f"mongodb+srv://{mongo_user}:{mongo_pass}@{domain}/{db_name}?retryWrites=true&w=majority", ssl=True)
