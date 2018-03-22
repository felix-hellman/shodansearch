import LoxoneSearch

LoxoneList = LoxoneSearch.Search()

for result in LoxoneList:
    print("IP ADDR: " + result.ip)
    print("VERSION: " + result.version)
    print("")
