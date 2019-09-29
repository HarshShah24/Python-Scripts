#! python 3

import request
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(res.status_code)
content = res.content
