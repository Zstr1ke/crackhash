import hashlib

passwd = input('Enter password: ')
hash = hashlib.sha256(passwd.encode('utf-8'))
print(f'Hashed {passwd} -->\n{hash.hexdigest()}')
