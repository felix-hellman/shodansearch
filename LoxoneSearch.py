import Auth
import shodan

api = shodan.Shodan(Auth.KEY)

try:
    results = api.search('Server: Loxone',page=2)
    print('Results found %s' % results['total'])
    for result in results['matches']:
        print('IP: %s' % result['ip_str'])
        startIndex = result['data'].find('Server:',0,len(result['data']))
        endIndex = result['data'].find("\n",startIndex,len(result['data']))
        print(result['data'][startIndex:endIndex:])
        print ('')
except (shodan.APIError, e):
    print ('Error: %s' % e)
