from django.db import models
from mongoTools.classes.methylation import Methylation
from mongoTools.base.mongo_engine import MongoEngine

def checkPosition(_id,database):
    checkPos = ""

    MongoEngine().set_database_name(database)
    checkPos = Methylation().find({'_id': _id})
    print (checkPos)