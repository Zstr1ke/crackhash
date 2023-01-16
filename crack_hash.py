dictionary = {}

with open('passwords.txt', 'r') as o:
	passwd = o.read().splitlines()


with open('breach.txt', 'r') as o:
	text = o.read().splitlines()
	for user_hash in text:
		username = user_hash.split(':')[0]
		hash = user_hash.split(':')[1]
		dictionary[username] = hash

import hashlib

for password in passwd:
	hashed_passwd = hashlib.sha256(password.encode('utf-8')).hexdigest()
	for username, hash in dictionary.items():
		if hashed_passwd == hash:
			print(f'Hash found:/\n{username}:{password}\n/')
