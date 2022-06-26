#!/usr/bin/env python3
from lib import conn, prop
import requests as rq
import json as js
import subprocess
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
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
		r1 = rq.get(u1, param, headers=conn.header, timeout=10)
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
		print(f"""=> Judul : {title}\n""")
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
		
	def mn3():
		subprocess.run('clear')
		prop.menu3()
		inm = input("Masukkan Nomor Telepon : ")
		phone = phonenumbers.parse(inm)
		Country_Code = phonenumbers.format_number(phone, phonenumbers.PhoneNumberFormat.INTERNATIONAL).split(' ')[0]
		local_Number = phonenumbers.format_number(phone, phonenumbers.PhoneNumberFormat.E164).replace(Country_Code, '')
		international_Number = phonenumbers.format_number(phone, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
		print('\nFormat Internasional : {}'.format(international_Number))
		print('\nFormat Lokal : 0{}'.format(local_Number))
		print('\nKode Negara : {}'.format(Country_Code))
		print('\nLokasi : {}'.format(geocoder.description_for_number(phone, 'id')))
		print('\nProvider : {}'.format(carrier.name_for_number(phone, 'id')))
		print('\nArea : {}'.format(geocoder.description_for_number(phone, 'id')))
		for timezone_res in timezone.time_zones_for_number(phone):
			print('\nZona Waktu : {}'.format(timezone_res))
		
		if phonenumbers.is_possible_number(phone):
			print('\nNomor Valid dan Memungkinkan\n')
		else:
			print('\nNomor Valid tapi Mungkin Tidak Bisa\n')

def main():
	prop.banner()
	i = input("Pilih Menu : ")
	if i == "1":
		menu.mn1()
	elif i =="2":
		menu.mn2()
	elif i =="3":
		menu.mn3()
		
if __name__ == "__main__":
	main()