import urllib, urllib2
from binascii import b2a_base64
import bluetooth
import sys

def addGETdata(url, data):
    return url + '?' + urllib.urlencode(data)

running=1
thissensor="1"
lookupURL = 'http://yourdomainURL.com'
while running:
      
    print "performing inquiry..."
    try:
        nearby_devices = bluetooth.discover_devices(lookup_names = True)

        print "found %d devices" % len(nearby_devices)

        for addr, name in nearby_devices:
            print " UUID: %s NAME: %s" % (addr, name)
            dunPort = 0 
            obexPort = 0
            services = bluetooth.find_service(address=addr)
            if len(services) > 0:
                for svc in services:
                    var = svc["name"]
                    if var != None:
                        if "Dial" in var:
                            dunPort = svc["port"]
                            print "DUN port acquired"
                        elif "OBEX" in var:
                            obexPort = svc["port"]
                            print "OBEX port acquired"
                        else:
                            print "--iterating--"

            data = 0
            url = addGETdata(lookupURL,
                             [('thissensor', thissensor),('addr', addr),('name', name)])
            req = urllib2.Request(url)
            fd = urllib2.urlopen(req)
            data = fd.read(1024)
            if data == "1":
                print "Already added"
            elif data == "2":
                print "Added device"
    except IOError, e:
        print "No Bluetooth device nearby"