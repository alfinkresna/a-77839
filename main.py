__Author__ : "Alfin"
__Copyright__ : "© 2022 alfinkresna"

import subprocess
import json as js
import socket
import requests as rq
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from lib import conn, prop
	
class menu():
	def mn1():
		subprocess.run("clear", check=True)
		prop.menu1()
		try:
			iw = input("Masukkan Website : ")
			rep = iw.replace("https://","")
			sc = socket.gethostbyname(rep)
			u1 = conn.connect_1
			param = {
			'url': iw
			}
			r = rq.get(iw)
			r1 = rq.get(u1, param, headers=conn.header, timeout=10)
			res1 = js.loads(r1.text)
			
			print()
			
			server = r.headers["server"]
			status = res1["status"]
			title = res1["data"]["title"]
			description = res1["data"]["description"]
			lang = res1["data"]["lang"]
			author = res1["data"]["author"]
			publisher = res1["data"]["publisher"]
			
			print(f"""=> Status : {status}\n""")
			print(f"""=> Domain Ip : {sc}\n""")
			print(f"""=> Server : {server}\n""")
			print(f"""=> Titel : {title}\n""")
			print(f"""=> Deskripsi : {description}\n""")
			print(f"""=> Bahasa : {lang}\n""")
			print(f"""=> Author : {author}\n""")
			print(f"""=> Publisher : {publisher}\n""")
		except socket.gaierror as e:
			print(f"\n{e}")
		
	def mn2():
		subprocess.run("clear", check=True)
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
		tipe = res2[0]["type"]
		
		print(f"""=> Perusahaan : {company}\n""")
		print(f"""=> Alamat 1 : {addressL1}\n""")
		print(f"""=> Alamat 2 : {addressL2}\n""")
		print(f"""=> Alamat 3 : {addressL3}\n""")
		print(f"""=> Negara : {country}\n""")
		print(f"""=> Tipe : {tipe}\n""")
		
	def mn3():
		subprocess.run('clear', check=True)
		prop.menu3()
		try:
			inm = input("Masukkan Nomor Telepon : ")
			phone = phonenumbers.parse(inm)
			countryCode = phonenumbers.format_number(phone, phonenumbers.PhoneNumberFormat.INTERNATIONAL).split(' ')[0]
			local_Number = phonenumbers.format_number(phone, phonenumbers.PhoneNumberFormat.E164).replace(countryCode, '')
			international_Number = phonenumbers.format_number(phone, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
			print('\n=> Format Internasional : {}'.format(international_Number))
			print('\n=> Format Lokal : 0{}'.format(local_Number))
			print('\n=> Kode Negara : {}'.format(countryCode))
			print('\n=> Lokasi : {}'.format(geocoder.description_for_number(phone, 'id')))
			print('\n=> Provider : {}'.format(carrier.name_for_number(phone, 'id')))
			print('\n=> Area : {}'.format(geocoder.description_for_number(phone, 'id')))
			for timezone_res in timezone.time_zones_for_number(phone):
				print('\n=> Zona Waktu : {}'.format(timezone_res))
			
			if phonenumbers.is_possible_number(phone):
				print('\n=> Nomor Valid dan Memungkinkan\n')
			else:
				print('\n=> Nomor Valid tapi Mungkin Tidak Bisa\n')
		except phonenumbers.phonenumberutil.NumberParseException as e:
			print(f"\n{e}")

def main():
	prop.banner()
	i = input("Pilih Menu : ")
	if i == "1":
		menu.mn1()
	elif i =="2":
		menu.mn2()
	elif i =="3":
		menu.mn3()
	else :
		print("\n\t\t{!} Pilihan Salah")
		
if __name__ == "__main__":
	main()
