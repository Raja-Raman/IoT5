# Switch on/off an LED on ESP12E/ 8266
# Run esp2.ino on the 8266
# Find its IP address from its serial console print out
# curl 192.168.1.26/LED=ON 
# curl 192.168.1.26/LED=OFF 

import requests
import time

requests.packages.urllib3.disable_warnings()
base_url = 'http://192.168.1.26/LED='
url = None

flag = True

print ("Press ^C to quit...")
while True:
    try:
        if (flag):
            url = base_url+'ON' 
        else: 
            url = base_url+'OFF'  
        print (url)            
        requests.get(url)          
        flag = not flag        
        time.sleep(2)   
    except KeyboardInterrupt:
        	break
        	
print ('\nDone!')
 
	