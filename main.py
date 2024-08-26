import os
import sys
import time
import subprocess
from colorama import Fore, Style, init
from pystyle import Colors, Colorate, Write

# Initialize colorama
init(autoreset=True)

REQUIRED_PACKAGES = [
    'whois', 'instaloader', 'discord.py==1.7.3', 'emailrep', 'requests',
    'phonenumbers', 'pystyle', 'cloudscraper', 'fake_useragent', 'uuid',
    'fade', 'py-socket', 'aiohttp', 'selenium', 'holehe',
    'deep_translator', 'colorama', 'instaloader'
]

def install_packages(packages: list[str]):
    for package in packages:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    import os
    import sys
    import time
    import subprocess
    import utils.theme
except Exception as e:
    print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
    install_packages(REQUIRED_PACKAGES)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def animated_text(text, delay=0.05):
    for line in text.split('\n'):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        sys.stdout.write('\n')
        sys.stdout.flush()
        time.sleep(delay)

def box_text(text, color=Fore.GREEN, symbol='★'):
    border = f"{symbol} " * (len(text) + 4)
    boxed_text = f"""
{color}{border}
{symbol}  {text}  {symbol}
{border}{Style.RESET_ALL}
"""
    return boxed_text

def display_ascii_art(timer_text=""):
    art = f"""
{Fore.CYAN}
                          $$\     $$\                                 $$\                   $$$$$$\       $$$$$$\  
                          $$ |    \__|                                $$ |                 $$$ __$$\     $$  __$$\ 
$$$$$$\$$$$\  $$\   $$\ $$$$$$\   $$\        $$$$$$\   $$$$$$\   $$$$$$$ |      $$\    $$\ $$$$\ $$ |    \__/  $$ |
$$  _$$  _$$\ $$ |  $$ |\_$$  _|  $$ |      $$  __$$\ $$  __$$\ $$  __$$ |      \$$\  $$  |$$\$$\$$ |     $$$$$$  |
$$ / $$ / $$ |$$ |  $$ |  $$ |    $$ |      $$ /  $$ |$$ /  $$ |$$ /  $$ |       \$$\$$  / $$ \$$$$ |    $$  ____/ 
$$ | $$ | $$ |$$ |  $$ |  $$ |$$\ $$ |      $$ |  $$ |$$ |  $$ |$$ |  $$ |        \$$$  /  $$ |\$$$ |    $$ |      
$$ | $$ | $$ |\$$$$$$  |  \$$$$  |$$ |      \$$$$$$$ |\$$$$$$  |\$$$$$$$ |         \$  /   \$$$$$$  /$$\ $$$$$$$$\ 
\__| \__| \__| \______/    \____/ \__|       \____$$ | \______/  \_______|          \_/     \______/ \__|\________|
                                            $$\   $$ |                                                             
                                            \$$$$$$  |                                                             
                                             \______/                                                              

                            ╔═════════════════════════════╗
                            ║            v0.3             ║
                            ║                             ║
                            ╚═════════════════════════════╝

╔═════════════════════════════╦═════════════════════════════╦══════════════════════════════╗
║  [01] Soon!                 ║  [11] IP Information        ║  [21] Number Scrapper        ║               
║       (Discord)             ║        (OSINT)              ║       (Scrapper)             ║
╠═════════════════════════════╬═════════════════════════════╬══════════════════════════════╣
║  [02] Soon                  ║  [12] Email Information     ║  [22] Website Scrapper       ║             
║       (Discord)             ║        (OSINT)              ║       (Scrapper)             ║     
╠═════════════════════════════╬═════════════════════════════╬══════════════════════════════╣
║  [03] Clear DM              ║  [13] Number Information    ║  [23] Soon!                  ║
║       (Discord)             ║        (OSINT)              ║       (Generator)            ║                 
╠═════════════════════════════╬═════════════════════════════╬══════════════════════════════╣
║  [04] Group Spammer         ║  [14] Roblox ID Information ║  [24] CC Generator           ║
║       (Discord)             ║        (OSINT)              ║       (Generator)            ║
╠═════════════════════════════╬═════════════════════════════╬══════════════════════════════╣
║  [05] Server Info           ║  [15] SOON                  ║  [25] Obfuscator             ║
║       (Discord)             ║        (OSINT)              ║       (Other)                ║
╠═════════════════════════════╬═════════════════════════════╬══════════════════════════════╣
║  [06] Status Rotator        ║  [16] SOON                  ║  [26] Token Generator        ║
║       (Discord)             ║        (OSINT)              ║       (Discord)              ║
╠═════════════════════════════╬═════════════════════════════╬══════════════════════════════╣
║  [07] Token Checker         ║  [17] Dox Tracker           ║  [27] FiveM Scrapper         ║
║       (Discord)             ║        (OSINT)              ║       (Scrapper)             ║
╠═════════════════════════════╬═════════════════════════════╬══════════════════════════════╣
║  [08] Token Mass DM         ║  [18] Instagram Information ║  [28] Token Information      ║
║       (Discord)             ║        (OSINT)              ║       (Discord)              ║
╠═════════════════════════════╬═════════════════════════════╬══════════════════════════════╣
║  [09] Webhook Info          ║  [19] Nitro Generator       ║  [29] Theme Changer          ║
║       (Discord)             ║        (Generator)          ║       (Other)                ║
╠═════════════════════════════╬═════════════════════════════╬══════════════════════════════╣
║  [10] Webhook Spammer       ║  [20] Token Joiner          ║  [30] SOON                   ║
║       (Discord)             ║        (Discord)            ║       (Generator)            ║
╠═════════════════════════════╬═════════════════════════════╬══════════════════════════════╣
║  [31] Chatbot               ║                             ║                             ║
║       (Custom)              ║                             ║                             ║
╚═════════════════════════════╩═════════════════════════════╩══════════════════════════════╝

╔═════════════════════════════╗
║        soon            ║
║                             ║
╚═════════════════════════════╝

╔═════════════════════════════╗
║  this tool is in beta!      ║ 
║                             ║
║   op paid discord tool!     ║
╚═════════════════════════════╝

{Style.RESET_ALL}
"""
    animated_text(art, delay=0)

def execute_script(script_name):
    script_path = os.path.join('utils', f'{script_name}')
    try:
        subprocess.run(['python', script_path], check=True)
        print(box_text(f"{Fore.GREEN}Executed {script_name} successfully!{Style.RESET_ALL}", color=Fore.GREEN))
    except subprocess.CalledProcessError as e:
        print(box_text(f"{Fore.RED}Error executing script '{script_name}': {e}{Style.RESET_ALL}", color=Fore.RED))

def main():
    clear()
    display_ascii_art()
    username = os.getlogin()

    while True:
        prompt = f"""
{Fore.CYAN}╭─── {Fore.WHITE}  {Fore.YELLOW}Please choose an option:{Style.RESET_ALL}
│
╰─/  {Style.RESET_ALL}"""
        choice = input(prompt).strip()

        if choice in ['1', '2', '15', '16', '23', '30']:
            print(f"{Fore.MAGENTA}This is not out yet!{Style.RESET_ALL}")
        elif choice == '3':
            execute_script('clear_dm.py')
        elif choice == '4':
            execute_script('group_spammer.py')
        elif choice == '5':
            execute_script('server_info.py')
        elif choice == '6':
            execute_script('status_rotator.py')
        elif choice == '7':
            execute_script('token_checker.py')
        elif choice == '8':
            execute_script('token_massdm.py')
        elif choice == '9':
            execute_script('webhook_info.py')
        elif choice == '10':
            execute_script('webhook_spammer.py')
        elif choice == '11':
            execute_script('ip_info.py')
        elif choice == '12':
            execute_script('email_info.py')
        elif choice == '13':
            execute_script('number_info.py')
        elif choice == '14':
            execute_script('roblox_id_info.py')
        elif choice == '15':
            print(f"{Fore.MAGENTA}This is not out yet!{Style.RESET_ALL}")
        elif choice == '16':
            print(f"{Fore.MAGENTA}This is not out yet!{Style.RESET_ALL}")
        elif choice == '17':
            execute_script('dox_tracker.py')
        elif choice == '18':
            execute_script('instagram_info.py')
        elif choice == '19':
            execute_script('nitro_generator.py')
        elif choice == '20':
            execute_script('token_joiner.py')
        elif choice == '21':
            execute_script('number_scrapper.py')
        elif choice == '22':
            execute_script('website_scrapper.py')
        elif choice == '24':
            execute_script('cc_generator.py')
        elif choice == '25':
            execute_script('obfuscator.py')
        elif choice == '26':
            execute_script('token_generator.py')
        elif choice == '27':
            execute_script('fivem_scrapper.py')
        elif choice == '28':
            execute_script('token_information.py')
        elif choice == '29':
            execute_script('theme_changer.py')
        elif choice == '30':
            print(f"{Fore.MAGENTA}This is not out yet!{Style.RESET_ALL}")
        elif choice == '31':
            chatbot_script = 'chatbot.py'
            execute_script(chatbot_script)
        else:
            print(f"{Fore.RED}Invalid choice! Please select a valid option.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
