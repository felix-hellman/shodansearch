import Auth
import shodan
import re

api = shodan.Shodan(Auth.KEY)
class LoxoneResult:
    version = ""
    ip = ""

digit = ['0','1','2','3','4','5','6','7','8','9']
def findDigit(inputString):
    for x in range(0,len(inputString)-1):
        for d in digit:
            if inputString[x] is d:
                return x

def Search():
    results = ''
    resultList = []
    try:
        results = api.search('Server: Loxone',page=2)
        #print('Results found %s' % results['total'])
        for result in results['matches']:
            r = LoxoneResult()
            #print('IP: %s' % result['ip_str'])
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
