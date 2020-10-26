from django.db import models
from mongoTools.classes.databaseContent import Content
from mongoTools.base.mongo_engine import MongoEngine

def getDBContent(database):
    content = ""

    MongoEngine().set_database_name(database)
    content = Content().find()

    return content.data