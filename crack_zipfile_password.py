import os, time

file = input('Please enter the zip file name: \n')
c = "/usr/sbin/zip2john %s > out.txt" %file

try:
	os.popen(c)
	print("zip file hash created")

except:
	print('zip file does not exist')
	exit()

os.popen('john --wordlist=rockyou.txt out.txt > result')
time.sleep(5)

f = open('result')
print(f)
for line in f:
	line = line.rstrip()
	if line.startswith('Loaded'):
		continue
	elif line.startswith('No'):
		print('the password was detected previously, please check /root/.john/*.pot')
		exit()
	pwd = line.split()
	print('Password is: ', pwd[0])

exit()
