from django.db import models
from mongoTools.classes.methylation import Methylation

def checkPosition(_id):
    checkPos = ""
    checkPos = Methylation().find({'_id': _id})
    print (checkPos)