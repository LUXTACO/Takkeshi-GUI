import requests
import re
import os
from colored import fg
color = fg('magenta')
print("")
print (color + """ ███▄    █  ▒█████  ▒██   ██▒ ██▓███   ██▓     ▒█████   ██▓▄▄▄█████▓
 ██ ▀█   █ ▒██▒  ██▒▒▒ █ █ ▒░▓██░  ██▒▓██▒    ▒██▒  ██▒▓██▒▓  ██▒ ▓▒
▓██  ▀█ ██▒▒██░  ██▒░░  █   ░▓██░ ██▓▒▒██░    ▒██░  ██▒▒██▒▒ ▓██░ ▒░
▓██▒  ▐▌██▒▒██   ██░ ░ █ █ ▒ ▒██▄█▓▒ ▒▒██░    ▒██   ██░░██░░ ▓██▓ ░ 
▒██░   ▓██░░ ████▓▒░▒██▒ ▒██▒▒██▒ ░  ░░██████▒░ ████▓▒░░██░  ▒██▒ ░ 
░ ▒░   ▒ ▒ ░ ▒░▒░▒░ ▒▒ ░ ░▓ ░▒▓▒░ ░  ░░ ▒░▓  ░░ ▒░▒░▒░ ░▓    ▒ ░░   
░ ░░   ░ ▒░  ░ ▒ ▒░ ░░   ░▒ ░░▒ ░     ░ ░ ▒  ░  ░ ▒ ▒░  ▒ ░    ░    
   ░   ░ ░ ░ ░ ░ ▒   ░    ░  ░░         ░ ░   ░ ░ ░ ▒   ▒ ░  ░      
         ░     ░ ░   ░    ░               ░  ░    ░ ░   ░           
                                                                     """)

def get_url():
    url = input("Enter the url of the site to scan: ")
    return url

def scan_site(url):
    # get the source code of the site
    source_code = requests.get(url)
    # convert the source code to plain text
    plain_text = source_code.text
    # find all the exploits in the source code
    exploits = re.findall(r'<script src="(.*?)"></script>', plain_text)
    return exploits

def print_exploits(exploits):
    print("The following exploits were found:")
    for exploit in exploits:
        print(exploit)

def get_protection_rating(exploits):
    if len(exploits) == 0:
        print("No exploits found!")
        return "Your site is well protected"
    elif len(exploits) <= 3:
        return "Your site is somewhat protected"
    else:
        return "Your site is not protected"

def main():
    url = get_url()
    exploits = scan_site(url)
    print_exploits(exploits)
    print(get_protection_rating(exploits))
    print("");
main()