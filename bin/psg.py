import random
import string
from colored import fg
import sys,time,random

typing_speed = 40 #wpm
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)


color = fg('red')


print (color + """\
 ██▓███   ▄▄▄        ██████   ██████  █     █░ ▒█████   ██▀███  ▓█████▄      ▄████ ▓█████  ███▄    █ 
▓██░  ██▒▒████▄    ▒██    ▒ ▒██    ▒ ▓█░ █ ░█░▒██▒  ██▒▓██ ▒ ██▒▒██▀ ██▌    ██▒ ▀█▒▓█   ▀  ██ ▀█   █ 
▓██░ ██▓▒▒██  ▀█▄  ░ ▓██▄   ░ ▓██▄   ▒█░ █ ░█ ▒██░  ██▒▓██ ░▄█ ▒░██   █▌   ▒██░▄▄▄░▒███   ▓██  ▀█ ██▒
▒██▄█▓▒ ▒░██▄▄▄▄██   ▒   ██▒  ▒   ██▒░█░ █ ░█ ▒██   ██░▒██▀▀█▄  ░▓█▄   ▌   ░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒
▒██▒ ░  ░ ▓█   ▓██▒▒██████▒▒▒██████▒▒░░██▒██▓ ░ ████▓▒░░██▓ ▒██▒░▒████▓    ░▒▓███▀▒░▒████▒▒██░   ▓██░
▒▓▒░ ░  ░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░░ ▓░▒ ▒  ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░ ▒▒▓  ▒     ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒ 
░▒ ░       ▒   ▒▒ ░░ ░▒  ░ ░░ ░▒  ░ ░  ▒ ░ ░    ░ ▒ ▒░   ░▒ ░ ▒░ ░ ▒  ▒      ░   ░  ░ ░  ░░ ░░   ░ ▒░
░░         ░   ▒   ░  ░  ░  ░  ░  ░    ░   ░  ░ ░ ░ ▒    ░░   ░  ░ ░  ░    ░ ░   ░    ░      ░   ░ ░ 
               ░  ░      ░        ░      ░        ░ ░     ░        ░             ░    ░  ░         ░ 
                                                                 ░                                   

=======================================================================================================
""")
def get_password_length():
    while True:
        try:
            password_length = int(input("Enter password length: "))
            if password_length < 1:
                print("Password length must be greater than 0")
            else:
                return password_length
        except ValueError:
            print("Password length must be an integer")

def generate_password(password_length):
    password = ""
    for i in range(password_length):
        password += random.choice(string.ascii_letters + string.digits)
    return password

def generate_passwords(password_length, number_of_passwords):
    passwords = []
    for i in range(number_of_passwords):
        passwords.append(generate_password(password_length))
    return passwords

def combine_passwords(passwords):
    combined_password = ""
    for password in passwords:
        combined_password += password
    return combined_password

def get_password_portion(combined_password, password_length):
    start_index = random.randint(0, len(combined_password) - password_length)
    end_index = start_index + password_length
    return combined_password[start_index:end_index]

def main():
    password_length = get_password_length()
    passwords = generate_passwords(password_length, 10)
    combined_password = combine_passwords(passwords)
    password = get_password_portion(combined_password, password_length)
    slow_type("Generating...")
    print("")
    time.sleep(1)
    slow_type("Done!")
    time.sleep(1)
    print("")
    if password_length >= 35:
      slow_type("Big password!")
      print("")
      slow_type("Instant Printing!")
      print("")
      print("")
      slow_type("Result: ")
      print(password)
    else:
      print("")
      slow_type("Result: ")
      slow_type(password);
      print("")
    print("Remember to Upvote!")

if __name__ == "__main__":
    main()