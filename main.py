import LoxoneSearch
import PowerLogicSearch
import CarGpsSearch

LoxoneList = LoxoneSearch.Search()
PowerLogicList = PowerLogicSearch.Search()
CarGpsList = CarGpsSearch.Search()

print("Loxone Smart Home Devices Found")
print("Ip\tVersion")
for result in LoxoneList:
    print(result.ip + "\t" + result.version)

print("PowerLogic Meters Found")
print("Ip")
for result in PowerLogicList:
    print(result.ip)

print("Car Gps Found")
print("Ip")
for result in CarGpsList:
    print(result.ip)
