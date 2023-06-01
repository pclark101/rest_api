# REST API test using Shodan 
from shodan import Shodan

#Creating writeable text file for output
info_shodan = open('host.txt', 'w')

#Hard-coded API key 
api = Shodan('API-key')

# Lookup an IP
ipinfo = api.host('8.8.8.8')
#print(ipinfo)

#Writes content of Google DNS to text file 
info_shodan.write(str(ipinfo))

#Closes text file 
info_shodan.close()



