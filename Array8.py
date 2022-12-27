from array import *
print('Bytes to Sreing: ')
array8 = array('b', [119,51,114,101,115,111,117,114,99,101])
s = array8.tobytes()
print(s)
x = array('b',[83,65,76,69,72])
d = x.tobytes()
print(d)