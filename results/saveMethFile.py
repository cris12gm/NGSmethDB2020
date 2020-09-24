import os

from django.conf import settings


def saveFileMeth(_id,meth,samplesOut):

    rootID = settings.MEDIA_ROOT+"/"+_id

    # Create dir
    os.mkdir(rootID)


    # f = open(fileNameAssociations,'w')

    # cabecera = "chrom\tchromStart"
    # for sample in samplesOut:
    #     cabecera = cabecera + "\t" + sample
    
    # print (cabecera)

    # for element in meth:
    #     chrom = element["_id"].split("_")[0]
    #     start = element["_id"].split("_")[1]
    #     escribir = chrom+"\t"+start
    #     for sample in samplesOut:
    #         try:
    #             escribir = escribir + "\t"+element['methylation_CG'][sample]['methRatio']
    #         except:
    #             escribir = escribir + "\t"+"NA"
    #     escribir = escribir + "\n"
    #     print (escribir)

    return meth