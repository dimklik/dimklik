from termcolor import colored
import os, requests, optparse

print(colored("""
 #################################################################################
 #                                                                               #
 #                            Telegram : @tajhackers                             #
 #                                                                               #
 #     ____________________@___________________________________________________  #
 #    /__  __ //   \      | |        / / / /   | / ____/ //_// ____/ __ \/ ___/  #
 #      / /   / /_\ \     | | ______/ /_/ / /| |/ /   / ,<  / __/ / /_/ /\__ \   #
 #     / /   /  ___  \    | | _____/ __  / ___ / /___/ /| |/ /___/ _, _/___/ /   #
 #    /_/   /_/     \_\ __/ /     /_/ /_/_/  |_\____/_/ |_/_____/_/ |_|/____/    #
 #                      ___/                                                     #
 #					                                                             #
 #                            @TAJ_CYBER_SECURY                                  #              
 #################################################################################
""", 'blue'))

parser = optparse.OptionParser(colored('\n\n [*] python3 AdminFinder.py <Target> -w <wordlist> ', 'red'))

parser.add_option('-u', '--url', dest='url', help='-u or --url | Masalan : -u <Target>')
parser.add_option('-w', '--wordlist', dest='wordlist', help='-w or --wordlist | Masalan : -w <wordlist.txt>')

(options, arguments) = parser.parse_args()

if not options.url:
    print(colored(f'[-] Iltimos URL-ni tekshiring: ', 'red'))
    exit('Error')
elif not options.wordlist:
    print(colored(f'[-] Iltimos wordlist kiriting: ', 'red'))
    exit('Error')

try:

    wordlist = open(f'{options.wordlist}', 'r')
    mylist = [line.rstrip('\n') for line in wordlist]

except:
    print(colored(f'[-] Wordlist None:'))
    exit('None')
def scanner():

    for page in mylist:
        try:

            response = requests.get(f'{options.url}{page}')
            if response.status_code == 200:
                print(colored(f'[+] Ststus Code : {response.status_code} {response.reason} | Success: {options.url}{page}', 'green'))
            elif response.status_code != 200:
                print(colored(f'[-] Status Code : {response.status_code} {response.reason} | Error {options.url}{page}', 'red'))

        except ConnectionError:
            print(colored('Internet bilan muomo bor:', 'red'))

scanner()

