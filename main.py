import LoxoneSearch
import PowerLogicSearch
import CarGpsSearch
import AGFEOSearch
import os

resultFolder = "results"

if not os.path.exists(resultFolder):
    os.makedirs(resultFolder)

LoxoneList = LoxoneSearch.Search()
PowerLogicList = PowerLogicSearch.Search()
CarGpsList = CarGpsSearch.Search()
AGFEOList = AGFEOSearch.Search()

with open(resultFolder+"/"+LoxoneSearch.FileName,"a") as output:
    output.write(LoxoneSearch.Header)
    for result in LoxoneList:
        output.write(result.printFormat())

with open(resultFolder+"/"+PowerLogicSearch.FileName,"a") as output:
    output.write(PowerLogicSearch.Header)
    for result in PowerLogicList:
        output.write(result.printFormat())

with open(resultFolder+"/"+CarGpsSearch.FileName,"a") as output:
    output.write(CarGpsSearch.Header)
    for result in CarGpsList:
        output.write(result.printFormat())

with open(resultFolder+"/"+AGFEOSearch.FileName,"a") as output:
    output.write(AGFEOSearch.Header)
    for result in AGFEOList:
        output.write(result.printFormat())
