import re

message = 'Harsh Shah 123-123-2343'

reExpression = re.compile(r'(\d\d\d)-\d\d\d-\d\d\d\d') #{} is used for Grouping
phoneNumber = reExpression.search(message)
if phoneNumber != None:
    print(phoneNumber.group(1))
else:
    print('Phone Number not found')


