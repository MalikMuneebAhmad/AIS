import math
import json
print (dir(math))
x = '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
print (y["city"])