import sys
import time
from colorama import Fore, init
import random

init()

print(f"{Fore.LIGHTYELLOW_EX}          _ ____________________")
print(f"{Fore.LIGHTYELLOW_EX}         | |		        \  ")
print(f"{Fore.LIGHTYELLOW_EX} ======> |-|---+ Endless +-------\  ")
print(f"{Fore.LIGHTYELLOW_EX} ======> |-|----+ death +--------/")
print(f"{Fore.LIGHTYELLOW_EX}         |_|____________________/")

while True:
    print(f"{Fore.LIGHTCYAN_EX}")
    menu = input(" [#] Select an action: ")
    if menu == "start":
        for i in range(101):
            time.sleep(0.3)
            sys.stdout.write(f"{Fore.LIGHTGREEN_EX}\r [$] We gain health: %a%%" % i)

        health = 100
        print(f"{Fore.LIGHTYELLOW_EX}\n [+] Your Health:", health)
        input()
        while health > 0:
            damage = random.choice([10, 5])
            health = health - damage
            print(f"{Fore.LIGHTRED_EX} [-] Lost", damage, "health")
            print(f"{Fore.LIGHTYELLOW_EX} [ ] Your Health:{Fore.LIGHTGREEN_EX}", health)
            input()
        print(f"{Fore.LIGHTRED_EX} [%] Game Over!")
    elif menu == "exit":
        print(f"{Fore.LIGHTWHITE_EX} [/] Goodbye...")
        sys.exit()
    elif menu == "help":
        print(f'''{Fore.LIGHTWHITE_EX}
                           /
                           |===================================|
                           |========                   ========/
            _______________________/                  /__________________________________________
 ||        / This game is a test platform that displays the work of different cheats. Commands: /
 ||========| [*] start - start the game _______________________________________________________/
 ||========| [x] exit - leave the game /
 ||        \__________________________/  ''')
    else:
        print(f"{Fore.LIGHTRED_EX} [!] Error: Invalid input!")
