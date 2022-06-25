#!/usr/bin/env python3
from lib import conn, prop
import requests as rq
import json as js
import subprocess
import socket
	
class menu():
	def mn1():
		subprocess.run("clear")
		prop.menu1()
		iw = input("Masukkan Website : ")
		rep = iw.replace("https://","")
		sc = socket.gethostbyname(rep)
		u1 = conn.connect_1
		param = {
		'url': iw
		}
		r1 = rq.get(u1, param,headers=conn.header, timeout=10)
		res1 = js.loads(r1.text)
		
		print()
		
		status = res1["status"]
		title = res1["data"]["title"]
		description = res1["data"]["description"]
		lang = res1["data"]["lang"]
		author = res1["data"]["author"]
		publisher = res1["data"]["publisher"]
		
		print(f"""=> Status : {status}\n""")
		print(f"""=> Domain Ip : {sc}\n""")
		print(f"""=> Titel : {title}\n""")
		print(f"""=> Deskripsi : {description}\n""")
		print(f"""=> Bahasa : {lang}\n""")
		print(f"""=> Author : {author}\n""")
		print(f"""=> Publisher : {publisher}\n""")
		
	def mn2():
		subprocess.run("clear")
		prop.menu2()
		icma = input("Masukkan MAC Address : ")
		u2 = conn.connect_2 + icma
		r2 = rq.get(u2, headers=conn.header, timeout=10)
		res2 = js.loads(r2.text)
		
		print()
		
		company = res2[0]["company"]
		addressL1 = res2[0]["addressL1"]
		addressL2 = res2[0]["addressL2"]
		addressL3 = res2[0]["addressL3"]
		country = res2[0]["country"]
		type = res2[0]["type"]
		
		print(f"""=> Perusahaan : {company}\n""")
		print(f"""=> Alamat 1 : {addressL1}\n""")
		print(f"""=> Alamat 2 : {addressL2}\n""")
		print(f"""=> Alamat 3 : {addressL3}\n""")
		print(f"""=> Negara : {country}\n""")
		print(f"""=> Tipe : {type}\n""")
	
def main():
	prop.banner()
	i = input("Pilih Menu : ")
	if i == "1":
		menu.mn1()
	elif i =="2":
		menu.mn2()
		
if __name__ == "__main__":
	main()
