import ipaddress
import re

from mongoTools.base.item import Item

class Methylation(Item):
    collection_name = 'methylation'
    collection_schema = {
        'methylation_CG': 1
    }

    def __init__(self):
        super(Methylation, self).__init__()
class Chroms(Item):
    collection_name= 'chromSizes'
    collection_schema = {
        'chrom' : 1,
        'size' : 1
    }

    def __init__(self):
        super(Chroms, self).__init__()