from django.db import models
from mongoTools.classes.methylation import Methylation,Chroms
from mongoTools.base.mongo_engine import MongoEngine

def getChroms(_chr,database):
    chroms = ""

    MongoEngine().set_database_name(database)
    chroms = Chroms().find({'chrom': _chr})
    return (chroms.data)