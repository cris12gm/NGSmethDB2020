from django.db import models

from mongoTools.base.mongo_engine import MongoEngine
from mongoTools.classes.methylation import Methylation
from mongoTools.classes.samples import Samples

# Create your models here.

def getRegionMeth(database,chrom,start,end):
    meth = ""
    methData = []

    MongoEngine().set_database_name(database)

    for i in range (start,end):
        _id = chrom+"_"+str(i)
        meth = Methylation().find({'_id': _id})
        meth = meth.data
        if meth:
            methData.append(meth)

    return methData

def getAllSamples(database):
    samples = ""

    MongoEngine().set_database_name(database)
    samples = Samples().find()

    return samples.data