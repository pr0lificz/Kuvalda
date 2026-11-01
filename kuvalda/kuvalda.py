import hashlib
import hashid
import argparse

def crack(target, wordlist):
    hash_length = {
        32: 'md5', 40: 'sha1', 64: 'sha256', 128: 'sha512' 
    }
    try:
        algorithm = hash_length.get(len(target))
        if algorithm is None:
            raise ValueError('Unsupported Hash Type')
        with open(wordlist, encoding='latin-1') as w:
            for word in w:
                word = word.strip()
                hashed_target = hashlib.new(algorithm, word.encode()).hexdigest()

                if hashed_target == target:
                    print(f'\033[32m[+] Match Found: {word}\033[0m')
                    return
            
        print(f'\033[31m[-] No Match Found: Wordlist Exhausted\033[0m')

    except ValueError as error:
        print(error)

def make_hash(text):
    print('Options\n1. md5\n2. sha1\n3. sha256\n4. sha512')
    hash_to_make = input('Select Algorithm From Options: ')

    if hash_to_make == '1':
        h = hashlib.new('md5')
    elif hash_to_make == '2':
        h = hashlib.new('sha1')
    elif hash_to_make == '3':
        h = hashlib.new('sha256')
    elif hash_to_make == '4':
        h = hashlib.new('sha512')
    else:
         print('Incorrect Input.')
         return

    h.update(text.encode())
    print(h.hexdigest())

def credits():
    print('''\033[31m
             %%%%%%%%%&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@@@@@@@
             %%%%%%%%%%%%%%%%%%&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
             %%%%%%%%%%%%%%%%%%%%%%%%%%%%&&&&&&%&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
             %%%%%%%%%%%#*,,(////((%%%%#/((((#(*((/((((###%%%%%&%%%%&%%%%%%&&&&&&&&&&&&&&&&&&
             ##((((#(((((((((/******///((((/(((((/(///(/(/(/(#%%%%%#%#%%%%%%%%%%%%%&&&&&&&&&&
             ((,,,****,*,**,***,,,,,*/**////(((//////////(((//*//****///,(#%%%%%%%%%%%%%%&&&&
             #((((#####(///***,,,,,,...,,.*//.,******/////,,,***,**,..,,.//((#####%%%%%%%%%%%
             ####(((###(((***,**,,,******,,....,.,,.,/(##%%%%%&&&%%%%%%##(/*,..,,,*/**/**/%%%
             ##########((/*//((///((/*,,,.,*,...,(%%%%%%%%%%%%%%%%%&&&&%%%%%%%#(*,**,,,,,,(##
             ((//((####(//(////////(((/////*,*#%%%%%%%&&&&%%%#%##%%&&&&&&%%%%%%%%(*,..,.,/((/
             ((#(((/(#(///**//**//**//*(((//#%%%%%%%&&&&&&&&&@&&&&&&&&&&&&&%%%%%%%%#*,,,,*//,
             (##(#((####(((///(((((/(((((((#%%%%&&&&&&&&&&@@@@@@@@@@@@@&&&&&&&%%%%%%#/*///**,
             %%%%%#%%%#%#####%%####((#((((#%%&&&&&&&&&@@@@@@@@@@@@@@@@@@@&&&&&&&&%%%%(****/((
             %%%###(**#%%%%%%%%%%%%%%%%%%##%&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&%%#(##(#/*
             #%%%#%#(#%%%%#%%%%%%&%%%%%%%##%&&&&@@@@&&&&%&&&&&&&&&&&@@@@@@@@@&&&&&&&%##%##%#(
             #############(###############&&@@@@&&%%%%%%%%%#%%%&&&%%%%&&&&@@@&&&&&&&%#%%%%%%#
             ##############(((((((((((#%&@@@@@&%%%%&&@@@&%#%%%%%%%%%%%%%%%%&&&&&&&&&%#%%%%%%%
             #########((((((((((((((%&@@@@@@@%%##%&@&&@@&&###%%%%%%#%&@@@@&%%&&@@@&&%########
             #######((((((((((((((#&&@@@@@@@&%%%%%%%&&&&%%%###%%#%%%&@@@@@&%%%&&&@@@&%#(#####
             ##########(((##(((##%&@@@@@@@@&&%%%%%%%%%#%%%##%%%%%%%%&&&@@@&%%%%&&@@@&&%######
             ################(#&&@@@@@@@@@&&&&%%%##########%%%%%#%%%%%%%%%%%%%%&&@@@@@&%#####
             ################&&@@@@@@@@@@@&&&%%%%%#(###%#%%%%%&%%%%%%%%%%%%%%%&&@@@@@@&&%####
             ##############%&@@@@@@@@@@@@&%%%%%%%######%%%%%%%%%%%%%%%%%%%%%&&&&@@@@@@@&&%###
             #############%&@@@@@@@@@@@@@@&&%%%%%%%%##%%%%%%%%%%%%%%%%%%%%%&&&&@@@@@@@@@&%%##
             #############&&@@@@@@@@@@@@@&&%%%%%%&%%%%%%%%%%%%%%%%%%%%%%%%&&&&&&@@@@@@@@@&&%#
             %%%%%%%%%##%&&&@@@@@@@@@@&&&%%&%&&&&&&&&%%%%%%##%%%%%%%%%&&&&&&&&&@@@@@@@@@@@&%%
             %%%%%%%%%%%%%%&&@@@@@@@&&%%%%%%&%%%%&&&&&&&&&&&&&&&&&&&&&&&&&&&&@@@@@@@@@@@@@@&&\nDev: pr0lificz\033[0m''')
    
def help():
    print('Kuvalda is a hashing tool.\nIt can id, crack and create hashes\nUsage\nid: python3 kuvalda.py id <hash>\ncrack: python3 kuvalda.py crack <hash> -w <wordlist>\nmake: python3 kuvalda.py make <text to hash> - wrap in "" for spaced text')
    
banner = '''
##    ## ##     ## ##     ##    ###    ##       ########     ###    
##   ##  ##     ## ##     ##   ## ##   ##       ##     ##   ## ##   
##  ##   ##     ## ##     ##  ##   ##  ##       ##     ##  ##   ##  
#####    ##     ## ##     ## ##     ## ##       ##     ## ##     ## 
##  ##   ##     ##  ##   ##  ######### ##       ##     ## ######### 
##   ##  ##     ##   ## ##   ##     ## ##       ##     ## ##     ## 
##    ##  #######     ###    ##     ## ######## ########  ##     ## '''

print(banner)

parser = argparse.ArgumentParser(
    prog='kuvalda',
    description='Kuvalda\nA basic hash identifier and cracker'
)

subparsers = parser.add_subparsers(dest='action', required=True)

id_parser = subparsers.add_parser('id', help='identify hash type')
id_parser.add_argument('hash', help='the target hash')

crack_parser = subparsers.add_parser('crack', help='crack hash', add_help=False,)
crack_parser.add_argument('hash', help='target hash')
crack_parser.add_argument('-w', required=True, metavar='WORDLIST', help='path to wordlist')

make_parser = subparsers.add_parser("make", help="turn characters into a hash")
make_parser.add_argument('text', help='characters to hash')

credits_parser = subparsers.add_parser('credits', help='show credits')

help_parser = subparsers.add_parser('help', help='show help / usage')
args = parser.parse_args()

if args.action == "id":
    hashID = hashid.HashID()
    print(f"[*] Possible types for {args.hash}:")
    for match in hashID.identifyHash(args.hash):
        print(f"Hash Type: {match.name}")
elif args.action == "crack":
    print(f"[*] Attempting: {args.hash}")
    crack(args.hash, args.w)
elif args.action == "make":
    make_hash(args.text)
elif args.action == "credits":
    credits()
elif args.action == "help":
    help()

    

