import urllib2
import urllib
import sys
import time
import random
import re
import os
os.system("clear")
#Warna
B = '\033[1m' #Bold
R = '\033[31m' #Red
G = '\033[32m' #Green
Y = '\033[33m' #Yellow
BL = '\033[34m' #Blue
P = '\033[35m' #Purple
W = '\033[37m' #White
U = '\033[2m' #Underline
N = '\033[0m' #Normal
#Pastikan Proxy List 1 Dir Dengan Script Python Ini
proxy_list = "proxylist.txt"
User-agent = "useragent.txt"

mesin = ['http://google.com','http://bing.com','http://facebook.com','http://twitter.com','http://yahoo.com']
print B+G+""
print " __         ______    ___    ___    __"
print "|  |       |  ____|   \  \  /  /   |  |"
print "|  |       | |____     \  \/  /    |  |"
print "|  |       |  ____|     \    /     |  |"
print "|  |_ __   | |____       \  /      |  |"
print "|__ __ _|  |______|       \/       |__|"
print B+R+""
print " __    __   ______       __       ______    "
print "|  \  |  | |  ____|     /  \     |   _  \   "
print "|    \|  | | |____     / __ \    |  |_|  |  "
print "|  |     | |  ____|   /      \   |   _  -   "
print "|  |\    | | |____   /  /__\  \  |  | \  \  "
print "|__|  \__| |______| /__/    \__\ |__|  \__\ "
time.sleep(2)
print B+BL+'#-----------------------------------------#'
print B+R+'           \!/LEVINEAR PYTHON\!/'
print B+BL+'#-----------------------------------------#'
ini_url = raw_input (B+Y+"[+] Masukan Url Visitor : ")
print ''
print B+Y+'[+] Url Visitor Anda => '+B+BL+'|'+B+W,ini_url
print B+BL+'#-----------------------------------------#'
def Autoclicker(proxy1):
    try:
	proxy = proxy1.split(":")
        print B+BL+"#-----------------------------------------#\n"+B+W+'[-]',proxy1, ""+B+P+"=> Process"+N
        time.sleep(2)
	proxy_set = urllib2.ProxyHandler({"http" : "%s:%d" % (proxy[0], int(proxy[1]))})
	opener = urllib2.build_opener(proxy_set, urllib2.HTTPHandler)
	opener.addheaders = [('User-agent', random.choice(User-agent)),
						('Refferer', random.choice(mesin))]
	urllib2.install_opener(opener)
	f = urllib2.urlopen(ini_url)
	#187034
	if "google.com" in f.read():
	   print B+G+"[*] Berhasil "+"\n"+B+BL+"#-----------------------------------------#\n"+N
	else:
	   print B+R+"[*] Link Gagal Di Kunjungi !\n"+B+BL+"#-----------------------------------------#\n"+N
           print B+R+"[!] Proxy / Connection Failed\n"+B+BL+"#-----------------------------------------#\n"+N
    except:
           print B+R+"[!] Proxy Error\n"+B+BL+"#-----------------------------------------#\n"+N
           time.sleep(5)
           pass

def loadproxy():
    try:
	get_file = open(proxy_list, "r")
	proxylist = get_file.readlines()
	count = 0
        proxy = []
	while count < len(proxylist):
	      proxy.append(proxylist[count].strip())
	      count += 1
        for i in proxy:
            Autoclicker(i)
    except IOError:
	print B+W+"\n[-] Error : Proxy List Tidak Ditemukan / Belum Dibuat\n"+N
	sys.exit(1)

def main():
   print """
"""+N
   loadproxy()
if __name__ == '__main__':
    main()
