import os 

os.system("tput setaf 2")
print("Verifying and Installing lvm2")
os.system("yum install lvm2")
os.system("rpm -qa |grep -i lvm")
os.system("lvm version")

