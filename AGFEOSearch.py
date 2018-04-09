
import Auth
import shodan

api = shodan.Shodan(Auth.KEY)
Header = "AGFEO Smart Home Devices\nIp\n"
FileName = "AGFEOSearchResult"
SearchString = 'ssl.cert.serial:"10293758115057549292"'

class AGFEOResult:
    ip = ""
    def printFormat(self):
        return self.ip + "\n"

def Search():
    results = ''
    resultList = []
    try:
        results = api.search(SearchString,page=1)
        pages = int((results['total'])/100)+1
        for x in range(1,pages+1):
            results = api.search(SearchString,page=x)
            for result in results['matches']:
                r = AGFEOResult()
                r.ip = result['ip_str']
                resultList.append(r)

    except (shodan.APIError, e):
        print ('Error: %s' % e)
    return resultList
