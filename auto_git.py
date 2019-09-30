import sys, os

os_ver = os.name
print(os_ver)

if os_ver == 'nt':
    os.system('CLS')
else:
    os.system('clear')

msg = input("Insert commit for push\n=>")

os.system('git add --all')
os.system('git commit -am "{}"'.format(msg))
os.system('git push')
