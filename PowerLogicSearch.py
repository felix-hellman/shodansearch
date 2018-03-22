import Auth
import shodan

api = shodan.Shodan(Auth.KEY)
class PowerLogicResult:
    ip = ""

def Search():
    results = ''
    resultList = []
    try:
        results = api.search('PowerLogic ION',page=1)
        for result in results['matches']:
            r = PowerLogicResult()
            r.ip = result['ip_str']
            resultList.append(r)
    except (shodan.APIError, e):
        print ('Error: %s' % e)
    return resultList
