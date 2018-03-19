import Auth
import shodan

api = shodan.Shodan(Auth.KEY)

try:
    results = api.search('Server: Loxone')

    print('Results found %s' % results['total'])
    for result in results['matches']:
        print('IP: %s' % result['ip_str'])
        print (result['data'])
        print ('')
except (shodan.APIError, e):
    print ('Error: %s' % e)
