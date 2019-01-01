import requests,os,time,sys
from multiprocessing.dummy import Pool
from colorama import Fore								
from colorama import Style								
from colorama import init
from platform import system
init(autoreset=True)
fr  =   Fore.RED
fh  =   Fore.RED
fc  =   Fore.CYAN
fo  =   Fore.MAGENTA
fw  =   Fore.WHITE
fy  =   Fore.YELLOW
fbl =   Fore.BLUE
fg  =   Fore.GREEN											
sd  =   Style.DIM
fb  =   Fore.RESET
sn  =   Style.NORMAL										
sb  =   Style.BRIGHT

tm= ('''{}{}\t   |__/  |__/   |__/   ''').format(fh,sb)+('''{}{}  |__/  |__/  |__/''').format(fg,sb)+('''{}{}|__/  |__/|______/''').format(fh,sb)
logo = '\n'+l+'\n'+t+'\n'+r+'\n'+k+'\n'+s+'\n'+se+'\n'+sk+'\n'+tm
def nadafa():
    if system() == 'Linux':
        os.system("clear")
    if system() == 'Windows':
        os.system('cls')
    else:
        pass
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:57.0) Gecko/20100101 Firefox/57.0"}
def intro(word,ok):
    nadafa()
    print '\n\n\n'
    print '\n\n\n'
    print '\n'
    #print logo
    #print '\n'
    print(ok)
    atx(word)
def nejmaf(site):
    print('{}{}[').format(fy,sb),('{}{}+').format(fg,sb),('{}{}]').format(fy,sb),('{}{}[Not Found...]').format(fr,sb),site
def nejmav(site):
    print('{}{}[').format(fy,sb),('{}{}+').format(fg,sb),('{}{}]').format(fy,sb),('{}{}[Found...]').format(fg,sb),site
def atx(s):
    for c in s + '\n':
        bb = ('{}{}'+c).format(fh,sb)
        sys.stdout.write(bb)
        sys.stdout.flush()
        time.sleep(4. / 60)

if system() == 'Windows':
    os.system('cls')
    os.system('title Coded By Lolicyndrome: Fast Apple checker v1')
elif system() == 'Android':
    os.system('clear')
elif system() == 'linux':
    os.system('clear')
else:
    pass
intro('\t\t\t     Coded By lolicyndrome','')
nadafa()
print '\n\n\n'+logo+'\n\n'
print ('{}{}\t\t\t\t\t   https://www.facebook.com/profile.php?id=100014204478368').format(fbl,sb)



class CheCker():
    def apple(self,i): #apple
        link = 'https://ams.apple.com/pages/SignUp.jsf'
        data = {'SignUpForm':'SignUpForm',
                'SignUpForm:emailField':i,
                'SignUpForm:blueCenter':'Continue',
                "javax.faces.ViewState":"j_id1"}
        s = requests.get(link)
        co = s.cookies.get_dict()
        r = requests.post(link,data=data,cookies=co)
        if 'already registered' in r.content:
            print ('{}{}[Apple......]: ').format(fg,sb),i
            with open("Apple.txt",'a') as am:
                am.writelines(i+'\n')
        else:
            print ('{}{}[Not Apple..]: ').format(fr,sb),i
    def ebay(self,i): #ebay but there problem of captcha
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:57.0) Gecko/20100101 Firefox/57.0"}
        link = 'https://fyp.ebay.com/EnterUserInfo?ru=https%3A%2F%2Fwww.ebay.com%2F&gchru=&clientapptype=19&rmvhdr=false'
        s = requests.get(link)
        co = s.cookies.get_dict()
        proxy = {'sock5':'95.110.224.30:38695'} #i did test with proxy but same problem
        data = {"ru":"https%3A%2F%2Fwww.ebay.com%2F",
                "showSignInOTP":"false",
                "signInUrl":"https://signin.ebay.com/ws/eBayISAPI.dll?SignIn&amp;otpFyp=1&amp;_trksid=l8610.p2059331",
                "clientapptype":"19",
                "reqinput":"8a4adcbb973c47eb07d4d739667d53f830872504a26451f3bc9cf232243c9bad",
                "rmvhdr":"false",
                "input":i}
        r = requests.post(link,headers=headers,data=data,cookies=co,proxies=proxy)
        if 'Enter a verification code to continue' in r.content:
            print 'captcha ebay '+i
        else:
            if "that's not a match" in r.content:
                print 'Not ebay '+i
            else:
                print 'ebay '+i
    def amazon(self,i): #amazon work 
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:57.0) Gecko/20100101 Firefox/57.0"}
        link = ""
        s = requests.get(link)
        co =  {"ubid-main":"131-4598931-1570945"}
        data = {"openid.identity":"ape:aHR0cDovL3NwZWNzLm9wZW5pZC5uZXQvYXV0aC8yLjAvaWRlbnRpZmllcl9zZWxlY3Q=",       
                "openid.assoc_handle":"ape:dXNmbGV4",
                "openid.mode":"ape:Y2hlY2tpZF9zZXR1cA==",
                "openid.claimed_id":"ape:aHR0cDovL3NwZWNzLm9wZW5pZC5uZXQvYXV0aC8yLjAvaWRlbnRpZmllcl9zZWxlY3Q=",
                "openid.ns":"ape:aHR0cDovL3NwZWNzLm9wZW5pZC5uZXQvYXV0aC8yLjA=",
                "email":i,
                "create":"0"}
        r = requests.post(link,headers=headers,data=data,cookies=co)
        if 'We cannot find an account' in r.content:
            print 'Not Amazon '+i
        else:
            print 'amazon '+it
            with open("Amazon.txt",'a') as am:
                am.writelines(i+'\n')
    def All_in_one(self,i):
        try:
            i = i.rstrip()
            checker.apple(i)
        except:
            pass
        



checker = CheCker()
#ok = ['tepot.3003@gmail.com']

if __name__=='__main__':
    ok = raw_input(('{}{}[-]Put Maillist: ').format(fy,sb))
    ok = open(ok,'r')
    speed = raw_input(("{}{}[-]Enter Speed: ").format(fy,sb))
    ThreadPool = Pool(int(speed))
    Threads = ThreadPool.map(checker.All_in_one, ok)
    















    
