import sys, os

os_ver = os.name
print(os_ver)

if os_ver == 'nt':
    os.system('CLS')
else:
    os.system('clear')

msg = 'git commit -am'
msg += input("Insert commit for push\n=>")

os.system('git add --all')
os.system(msg)
