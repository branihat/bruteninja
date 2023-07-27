import requests
from time import sleep
from colorama import Back, Fore, init
import sys
import tqdm as tqdm
import logging
import os
os.system("cls")

line = Fore.YELLOW + '''
========================================================================================================
'''
print(line)
banner = print(Fore.RED + '''
   #----------------------------------------------------------------------------------------------#
   #                                                                                              #
   #      ▄▄▄▄▄▄▄ ▄▄▄▄▄▄   ▄▄   ▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄    ▄▄    ▄ ▄▄▄ ▄▄    ▄     ▄▄▄ ▄▄▄▄▄▄▄         #
   #      █  ▄    █   ▄  █ █  █ █  █       █       █  █  █  █ █   █  █  █ █   █   █       █       # 
   #      █ █▄█   █  █ █ █ █  █ █  █▄     ▄█    ▄▄▄█  █   █▄█ █   █   █▄█ █   █   █   ▄   █       # 
   #      █       █   █▄▄█▄█  █▄█  █ █   █ █   █▄▄▄   █       █   █       █▄  █   █  █▄█  █       # 
   #      █  ▄   ██    ▄▄  █       █ █   █ █    ▄▄▄█  █  ▄    █   █  ▄    █ █▄█   █       █       # 
   #      █ █▄█   █   █  █ █       █ █   █ █   █▄▄▄   █ █ █   █   █ █ █   █       █   ▄   █       # 
   #      █▄▄▄▄▄▄▄█▄▄▄█  █▄█▄▄▄▄▄▄▄█ █▄▄▄█ █▄▄▄▄▄▄▄█  █▄█  █▄▄█▄▄▄█▄█  █▄▄█▄▄▄▄▄▄▄█▄▄█ █▄▄█       # 
   #                                                                                              #
   #----------------------------------------------------------------------------------------------#
		''' + Fore.WHITE + '''
	                              +-+ Codded By VISHNU_THANDEL +-+
	                                  +-+ Team VTECH_ACER_ZONE +-+
	                           +-+ https://facebook.com/PakBlackArmy +-+
'''+ Fore.RED +'''                                    / _ \_______________/`/\+-/\`\`\`
                                  \_\(_)/_/ BRUTE_NINJA -+-    -+-+-
                                 _/`/`o`\`\_            \`\/+-\/`/`/
                                    /   \                \/-+--\/`/ ''')

print(line)


# def start():
#     avatar = Fore.BLUE + "[" + Fore.RED + "+" + Fore.BLUE + "] " + Fore.WHITE
#     target_url = input(Fore.GREEN +"Enter Target URL : "+ Fore.WHITE)
#     print(avatar + "Starting Attack On : ",target_url)
#     print(avatar + "Loading Wordlist...")
#     wordlist = get_wordlist()
#     with open(wordlist, "r") as f:
#         wordlist = f.readlines()
    
#     timeout = int(input("Enter Timeout Value in Seconds: "))
#     threads = int(input("Enter Number of Threads: "))
    
#     with tqdm.tqdm(total=len(wordlist)) as pbar:
#         for word in wordlist:
#             path_of_url = "http://" + target_url + word.strip()
#             try:
#                 get_url = requests.get(path_of_url,timeout=timeout).status_code
#                 pbar.update()
#                 if get_url == 200:
#                     found = 1
#                     url_size = requests.head(path_of_url).headers.get("Content-Length")
#                     if url_size is not None:
#                         with open("results.txt", "a") as f:
#                             f.write(path_of_url + "\n")
#                         print(avatar + Fore.WHITE + "Found!" + f"{path_of_url} => {url_size} Bytes" + "\n")
#             except requests.exceptions.ConnectionError:
#                 pass            
#             except KeyboardInterrupt:
#                 print("Program interrupted by user.")
#                 break


# def get_wordlist():
#     if len(sys.argv) == 1:
#         return "wordlist.txt"
#     else:
#         return sys.argv[1]


# if __name__ == "__main__":
#     start()



def start():
    avatar = Fore.BLUE + "[" + Fore.RED + "+" + Fore.BLUE + "] " + Fore.WHITE
    target_url = input(Fore.GREEN +"Enter Target URL :"+ Fore.WHITE)
    print(avatar + "Starting Attack On : ",target_url)
    wordlist = "D:\Desktop\proj\Tools\Brute_Ninja\BruteNinja\wordlist.txt"
    if not os.path.isfile(wordlist):
        print(avatar + "Error: Wordlist file does not exist!")
        sys.exit(1)

    if not os.access(wordlist, os.R_OK):
        print(avatar + "Error: Wordlist file is not readable!")
        sys.exit(1)

    with open(wordlist, "r") as f:
        wordlist = f.readlines()


# def check_url_status():
#     try:
#         requests.get(target_url, timeout=timeout)
#         return True
#     except requests.exceptions.ConnectionError:
#         return False
#     if not check_url_status():
#         print(avatar + "Target URL is not up and running!")
#         exit()
#     else:
#         attack()

    timeout = int(input("Enter Timeout Value in Seconds: "))
    threads = int(input("Enter Number of Threads: "))
# def attack():
    with tqdm.tqdm(total=len(wordlist)) as pbar:
        for word in wordlist:
            path_of_url = "http://" + target_url + word.strip()
            try:
                get_url = requests.get(path_of_url,timeout=timeout).status_code
                pbar.update()
                if get_url == 200:
                    found = 1
                    url_size = requests.head(path_of_url).headers.get("Content-Length")
                    if url_size is not None:
                        with open("results.txt", "a") as f:
                            f.write(path_of_url + "\n")
                        print(avatar + Fore.WHITE + "Found!" + f"{path_of_url} => {url_size} Bytes" + "\n")
            except requests.exceptions.ConnectionError:
                print("A Connection error occured.")
            except KeyboardInterrupt:
                print("Program interrupted by user.")
                break
            except Exception as e:
                print(f"[!] Error: {e}")

if __name__ == "__main__":

    start()

