from django.db import models
from mongoTools.classes.methylation import Methylation
from mongoTools.classes.chroms import Chroms
from mongoTools.classes.samples import Samples
from mongoTools.base.mongo_engine import MongoEngine

def getAllChroms(database):
    chroms = ""

    MongoEngine().set_database_name(database)
    chroms = Chroms().find()
    
    return chroms.data

def getAllSamples(database):
    samples = ""

    MongoEngine().set_database_name(database)
    samples = Samples().find()

    return samples.data