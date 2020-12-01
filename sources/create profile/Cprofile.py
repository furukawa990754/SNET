import subprocess
import os
import pickle
import copy
import hashlib
import base64
print('')
try:
    from subprocess import DEVNULL
except ImportError:
    DEVNULL = os.open(os.devnull, os.O_RDWR)
c=subprocess.Popen("VBoxManage list vms", stdin=DEVNULL, stdout=subprocess.PIPE,stderr=DEVNULL,shell=True).communicate()[0]
b=c.decode('utf-8')
name=b.replace("\r\n","\n")
print(name)
print('')
name=input(' プロファイルプロファイルに追加したい仮想マシン名を入力>> ')
try:
    path="./resources/profile/"+name+".dat"
    uuid=input(' UUIDを入力 {}を含める >> ')
    hashd = hashlib.md5(uuid.encode() ).hexdigest()
    uuid=base64.b64encode(uuid.encode())
    intf=[uuid,hashd]
    with open(path, 'wb') as web:
      pickle.dump(intf , web)
except:
    pass
#os.getlogin()
ddf=hashlib.md5(os.getlogin().encode()).hexdigest()
with open("user.dat", 'wb') as web:
  pickle.dump(ddf , web)
