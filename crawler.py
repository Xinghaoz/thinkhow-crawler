import requests
import re

r = requests.get("http://www.meilishuo.com")
#print r.text

pattern = re.compile('[a-zA-z]+://[^\s]*')
print pattern.findall(r.text)
