import os 
import sys
import fileinput 


os.system("tput setaf 2" )
print("\t\t\t WELCOME TO THE AUTOMATION SCRIPT BY th3gentleman-MubinGirach")
os.system("tput setaf 7")
print("\t\t\t-------------------------------------------------------")
os.system("tput setaf 3")
print("""
\n
Hola User !
Press 1:To setup and mount LVM 
Press 2 :To configure the LVM as your Datanode drive
Press 3:To resize the LVM
 """) 

os.system("tput setaf 7")
option=input("Enter your choice: ")
print(option)

if int(option) == 1:
	
	os.system("tput setaf 1")
	print("This is the list of Disks you have")
	os.system("fdisk -l")
	os.system("tput setaf 4")
	print("----------------------------------")

	ch=input("You want to create LVM  parition in which disk ?: ")
	print(ch)
	b="pvcreate"+" "+ch
	print(b)
	os.system(b)
	os.system("pvdisplay")
	
	os.system("tput setaf 7")
	vgcreate=input("Enter the name of the VOLUME GROUP: ")
	print(vgcreate)
	c="vgcreate"+" "+vgcreate+" "+ch
	os.system(c)
	
	os.system("tput setaf 7")
	lvname=input("Enter the name of the LOGICAL VOLUME:")	
	print(lvname)
	lvsize=input("Enter the size of LOGICAL VOLUME IN G-GB ,M-MB,K-KB :")
	print(lvsize)
	lvcreate="lvcreate"+" "+"--size"+" "+lvsize+"--name"+lvname+" "+vgcreate
	os.system(lvcreate)
	os.system("lvdisplay")
	
	os.system("tput setaf 7")
	print("Lets mount the LVM into a dir")
	directory=input("So what should be the name of the directory:")
	print(directory)
	mkdir="mkdir"+" "+directory
	os.system(mkdir)
	format="mkfs.ext4"+" "+"/dev/"+vgcreate+"/lvol0"
	os.system(format)
	print("Please wait mounting the LVM to the directory given")
	mount="mount"+" "+"/dev/"+vgcreate+"/"+"lvol0"+" "+directory
	os.system(mount)
	print("Sucessfully mounted")
	
	os.system("tput setaf 1")
	os.system("tput setaf 7")
	
         

elif int(option) == 3:
	

	os.system("tput setaf 6")	
	os.system("vgdisplay")
	vg=input("Enter the Volume Group: ")
	print(vg)
	os.system("lvdisplay")
	print("Thanks for the input wait while we find the location")
	extend=input("OK user tell me how much you want the extend in K-KB,M-MB,G-GB DONT EXCEED THE SIZE OF VOLUME GROUP :) :")
	print(extend)
	lvextnd="lvextend"+" "+"--size"+" "+"+"+extend+" "+"/dev/"+vg+"/"+"lvol0"
	os.system(lvextnd)
	resize2fs="resize2fs"+" "+"/dev/"+vg+"/"+"lvol0"
	os.system(resize2fs)
	os.system("tput setaf 3")
	os.system("lvdisplay")
	os.system("tput setaf 6")
	print("LVM EXTENDED ENJOY !!!")
	os.system("tput setaf 3")
	print("OK,Thanks for using the script by th3gentleman-MubinGirach")
	os.system("tput setaf 7")
	
	


elif int(option) == 2:
	
	print("Hope so you have setup the Hadoop Datanode i will just add this dynamic partition in a bit")
	textToReplace =input("Enter the directory of the folder you want configure as Datanode drive in the form of /root/folder_name: ")
	print(textToReplace)
	textToSearch =input("Please enter the exisiting folder used for Datanode storage: ")
	print(textToSearch)

	fileToSearch = '/etc/hadoop/hdfs-site.xml'
	tempFile = open( fileToSearch, 'r+' )
	for line in fileinput.input( fileToSearch ):
   		tempFile.write( line.replace( textToSearch, textToReplace))
	tempFile.close()
	
	print("Done please start your Datanode now..")
    
	
	


else:
	os.system("tput setaf 1")
	print("Please enter a valid option")
	os.system("tput setaf 7")
	



	










