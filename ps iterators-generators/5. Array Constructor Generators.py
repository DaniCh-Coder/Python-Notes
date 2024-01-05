# Generators
# Array Constructor Examples
# The array construcor takes two arguments, so the parenthesis aroun the generator expression are mandatory.
# The first argument of the array constructor defnes the storage type used for the numberr in the array
import array

symbols = '$¢£¥€¤'
array.array('I', (ord(symbol) for symbol in symbols))

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
for tshirt in ((c, s) for c in colors for s in sizes):
    col, size = tshirt # tuple unpacking
    print(col, size)
    
# Inicialize a list of points in pyton there the y coordinate is double the x coordinate and the x coordinate is increasing from 0 to 5
l =[]
for i in range(6):
    m = {'x':i, 'y':i*2}
    l.append(m)
print(l)