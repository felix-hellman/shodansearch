import Auth
import shodan

api = shodan.Shodan(Auth.KEY)
class CarGpsResult:
    ip = ""

def Search():
    results = ''
    resultList = []
    try:
        results = api.search('port:23 gps "on console"',page=1)
        for result in results['matches']:
            r = CarGpsResult()
            r.ip = result['ip_str']
            resultList.append(r)
    except (shodan.APIError, e):
        print ('Error: %s' % e)
    return resultList
