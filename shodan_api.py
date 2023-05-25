# REST API Call test using Shodan 

from shodan import Shodan

info_shodan = open('host.txt', 'w')

api = Shodan('API-key')

# Lookup an IP
ipinfo = api.host('8.8.8.8')
#print(ipinfo)

info_shodan.write(str(ipinfo))


info_shodan.close()



