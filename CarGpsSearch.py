import Auth
import shodan

api = shodan.Shodan(Auth.KEY)
SearchString = 'port:23 gps "on console"'
Header = "C4Max Smart Box Found\nIp\n"
FileName = "CarGpsSearchResult"

class CarGpsResult:
    ip = ""
    def printFormat(self):
        return self.ip + "\n"

def Search():
    results = ''
    resultList = []
    try:
        results = api.search(SearchString,page=1)
        for result in results['matches']:
            r = CarGpsResult()
            r.ip = result['ip_str']
            resultList.append(r)
    except (shodan.APIError, e):
        print ('Error: %s' % e)
    return resultList
