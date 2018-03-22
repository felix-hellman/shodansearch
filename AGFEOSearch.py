
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
        for result in results['matches']:
            r = AGFEOResult()
            r.ip = result['ip_str']
            resultList.append(r)
    except (shodan.APIError, e):
        print ('Error: %s' % e)
    return resultList
