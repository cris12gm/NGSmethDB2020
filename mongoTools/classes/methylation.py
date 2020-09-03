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
