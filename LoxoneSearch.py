import Auth
import shodan
import re

api = shodan.Shodan(Auth.KEY)

Header = "Loxone Smart Home Server\nIp\tVersion Number\n"
SearchString = 'Server: Loxone'
FileName = "LoxoneSearchResult"

class LoxoneResult:
    version = ""
    ip = ""
    def printFormat(self):
        return str('' + self.ip + "\t" + self.version + "\n")


def findDigit(inputString):
    digit = ['0','1','2','3','4','5','6','7','8','9']
    for x in range(0,len(inputString)-1):
        for d in digit:
            if inputString[x] is d:
                return x

def Search():
    results = ''
    resultList = []
    try:
        results = api.search(SearchString,page=2)
        for result in results['matches']:
            r = LoxoneResult()
            r.ip = result['ip_str']
            serverIndex = result['data'].find('Server:',0,len(result['data']))
            endIndex = result['data'].find("\n",serverIndex,len(result['data']))
            stringsearch = result['data'][serverIndex:endIndex:]
            search = findDigit(stringsearch)
            r.version = stringsearch[search::]
            resultList.append(r)
    except (shodan.APIError, e):
        print ('Error: %s' % e)
    return resultList
