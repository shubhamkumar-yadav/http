import http.client
print("this program returns a list of methods is enabled \n")
host = input("insert the name of IP:")
port = input("insert the port:")
if (port==""):
    port=80
try:
    connection = http.client.HTTPConnection(host,port)
    connection.request('options','/')
    response = connection.getresponse()
    print("enabled methods are :",response.getheader('allow'))
    connection.close()
except ConnectionRefusedError:
    print("connection failed")        