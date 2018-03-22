import LoxoneSearch
import PowerLogicSearch

LoxoneList = LoxoneSearch.Search()
PowerLogicList = PowerLogicSearch.Search()

print("Loxone Smart Home Devices Found")
print("Ip\tVersion")
for result in LoxoneList:
    print(result.ip + "\t" + result.version)

print("PowerLogic Meters Found")
print("Ip")
for result in PowerLogicList:
    print(result.ip)
