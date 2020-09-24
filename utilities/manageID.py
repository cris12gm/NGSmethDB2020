import string
import random
import os
from django.conf import settings

def generate_uniq_id(size=15, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def checkID(_id):
    idPath = settings.MEDIA_ROOT + "/"+_id
    isDirectory = os.path.isdir(idPath)
    return (isDirectory)

