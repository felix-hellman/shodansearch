import LoxoneSearch
import PowerLogicSearch
import CarGpsSearch
import AGFEOSearch
import os

resultFolder = "results"

if not os.path.exists(resultFolder):
    os.makedirs(resultFolder)

def PerformSearch(Search):
    SearchList = Search.Search()
    with open(resultFolder+"/"+Search.FileName,"a") as output:
        output.write(Search.Header)
        for result in SearchList:
            output.write(result.printFormat())

PerformSearch(LoxoneSearch)
PerformSearch(PowerLogicSearch)
PerformSearch(CarGpsSearch)
PerformSearch(AGFEOSearch)
