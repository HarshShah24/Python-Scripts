import re

message = 'HF Create with 10 digit HF id : 1234567898'

hfRegex = re.compile(r'\d\d\d\d\d\d\d\d\d\d')
hfID = hfRegex.search(message)
if hfID != None:
    print(hfID.group())
else:
    print('No Match Found')

