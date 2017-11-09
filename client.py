import socket
import pickle

BUFFSIZE = 1024
print "Starting client prog"

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print "Socket successfully created."
except socket.error as err:
    print "Socket creation failed with error %s" %(err)

host = 'cs3.kennesaw.edu'
port = 12311



'''
Variables for data manipulation.
arg_val =  Argument value for request type E.
request_type = Type of request to be sent.
poly = List of numbers.
a = value a for bisection.
b = value b for bisection.
tol = tolerance in bisection.
'''

request_type = 'E'
arg_val = 1.0
poly = [631,232,223,222]
a = 3
b = 2
tol = 0.00000000001

request = [request_type, arg_val,' ', poly]
#request = [request_type, a, ' ', b, ' ', poly, ' ', tol]
s.connect((host, port))

pickle.dump(request, open("save.p", "wb"));

#s.send(request)
recieve = pickle.load(open("save.p", "rb"))
if (recieve[0] == 'E' or recieve[0] == 'S'):
    print(recieve)
elif (recieve[0] == 'X'):
    print(recieve)
s.close
