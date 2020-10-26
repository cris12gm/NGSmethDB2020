import os

from django.conf import settings
from .models import getAllSamples


def saveFileMeth(_id,meth,samplesOut):

    rootID = settings.MEDIA_ROOT+"/"+_id

    fileName = rootID+"/methFile.out"
    f = open(fileName,'w')

    if samplesOut == "ALL":
        samplesOut = []
        samplesD = getAllSamples("hg38")
        for sample in samplesD:
            samplesOut.append(sample['sample'])
    cabecera = "chrom\tchromStart"
    for sample in samplesOut:
        cabecera = cabecera + "\t" + sample
    f.write(cabecera+"\n")

    for element in meth:
        chrom = element["_id"].split("_")[0]
        start = element["_id"].split("_")[1]
        escribir = chrom+"\t"+start
        for sample in samplesOut:
            try:
                escribir = escribir + "\t"+element['methylation_CG'][sample]['methRatio']
            except:
                escribir = escribir + "\t"+"NA"
        escribir = escribir + "\n"
        f.write(escribir)
    f.close()

    linkFile = fileName.replace(settings.MEDIA_ROOT,settings.MEDIA_URL)
    return linkFile