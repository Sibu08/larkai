import subprocess
import sys

# print('starting...')
# p1=subprocess.run(['python', 'manage.py','runserver'],shell=True)
# print(p1) 
p=subprocess.call(['python', 'manage.py','runserver'], creationflags=subprocess.CREATE_NEW_CONSOLE)
print(p)

p2=subprocess.run(['python', 'push.py'],shell=True)
print(p2) 