# JSON(javascript object notation)( API BANATE HAI )
# it is mainly used for storing and transferring data between the browser and server.
# JSON is text,written with javascript object notation
# python too support JSON with a built in package called json (import json)
# JSON support mainly 6 data type :-- string, number ,boolean , null ,object ,array.

# CONVERTING PYTHON OBJECT TO JSON
# blog={'URL':'www.wscubetech.com','name':wscubetech'}
# to_json=json.dumps(blog)

import json

d = {
    'course name': 'python', 'fees': 15000
}
f = json.dumps(d)
print(type(f))
print(f)

# CONVERTING JSON TO PYTHON OBJECTS:---
# if you have a JSON string,you can parse it by using the json.loads()method.

import json
d = '{"cname":"python","fees":12000,"duration":2 months"}'

x=json.loads(d)
print(type(x))
print(x)
for a in x:
    print(a,x[a])