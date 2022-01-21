import random
import time
import string
import os
import pythonping
import colorama
import requests
from os import system
from colorama import init, Fore, Style
from random import randint
from random import choice
from random import randrange
from pythonping import ping

system(f'title FreeMoneyHubs Multi Tool')
print(f"{Fore.RED}▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
print("▐                                         FreeMoneyHubs Multi Tool                                           ▐")
print("▐                                         ------------------------                                           ▐")
print("▐   1 = Card Gen   2 = Email Gen                                                                             ▐")
print("▐                                                                                                            ▐")
print("▐   3 = Ip Pinger  4 = Ip Analyzer                                                                           ▐")
print("▐                                                                                                            ▐")
print("▐                                                                                                            ▐")
print("▐                                                                                                            ▐")
print("▐                                                                                                            ▐")
print("▐                                                                                                            ▐")
print("▐                                                                                                            ▐")
print("▐                                                                                                            ▐")
print(f"▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀{Style.RESET_ALL}")

menu3 = input(f"{Fore.LIGHTBLUE_EX}[?] : {Style.RESET_ALL}")
if menu3 == '1':
    num = input(f'{Fore.LIGHTBLUE_EX}[?] How Many Cards To Generate : {Style.RESET_ALL}')
    loopamm = int(num)
    frist = (['Travel: 3', 'Visa: 4', 'MasterCard: 5', 'Discover: 6'])
    second = (['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'])
    third = (['23', '24', '25', '26', '27'])
    with open(f"Cards{num}.txt", "w", encoding='utf-8') as filebb:

        for i in range(loopamm):
            gaminqds = randrange(100, 999)
            weareweare = randrange(1000, 9999)
            jejdjehdhhrh = randrange(1000, 9999)
            udjdhddhdhh = randrange(1000, 9999)
            hdidhdushsnd = randrange(100, 999)
            part1 = (random.choice(frist))
            part2 = (gaminqds)
            part3 = (weareweare)
            part4 = (jejdjehdhhrh)
            part5 = (udjdhddhdhh)
            part6 = (hdidhdushsnd)
            part7 = (random.choice(second))
            part8 = (random.choice(third))
            print(f'{Fore.GREEN}{Style.BRIGHT}({i}) - {part1}{part2}-{part3}-{part4}-{part5} {part7}/{part8} {part6}{Style.RESET_ALL}')
            filebb.write(f"{part1}{part2}{part3}{part4}{part5} {part7}/{part8} {part6}\n")
        with open(f"Cards{num}.txt") as filebb:
            for line in file.readlines():
                carddie = line.strip("\n")
                print("[!] Finished")

elif menu3 == '2':
    baiduj = input('[?] How Mail Emails To Make : ')
    with open(f"Emails{baiduj}.txt", "w", encoding='utf-8') as fileffs:
        jdjdjd = (['justin', 'james', 'juan', 'lopez', 'matt', 'bryan', 'tina', 'mark', 'mason', 'brass', 'jeff', 'caleb',
         'marten', 'willson', 'pro', 'old', 'oscar', 'asher', 'gaming', 'davis', 'noah', 'seth', 'trent', 'luke',
         'carson', 'ella', 'brook', 'tate', 'brice', 'collin', 'ryan','jamie','mega','ted','steve'])
        bbsi = (['@gmail.com', '@yahoo.com', '@hotmail.com'])
        inny23 = int(baiduj)
        time.sleep(.5)
        for i in range(inny23):
            partt0 = randrange(1, 999)
            partt1 = (random.choice(jdjdjd))
            partt2 = (random.choice(bbsi))
            print(f'({i}) - {partt1}{partt0}{partt2}')
            fileffs.write(f"{partt1}{partt0}{partt2} \n")
        with open(f"mails{baiduj}.txt") as filebb:
            for line in file.readlines():
                emaildie = line.strip("\n")
                print("[!] Finished")
elif menu3 == '3':
    ippp = input("[?] Enter Ip To Ping : ")
    ammo3unt = input("[?] Amount Of Times To Ping : ")
    nummies = int(ammo3unt)
    try:
        ping(f'{ippp}', count=nummies, verbose=True)
        time.sleep(1)
        print("[!] Finished")
    except:
        print(f"{Fore.RED}{Style.BRIGHT}[!] That Ip Is Not Possible To Even Have Retard{Style.RESET_ALL}")
elif menu3 == '4':
    aufsaifs = input("[?] Enter The Ip You Want To Get Info On : ")
    daaataaa = requests.get(f"http://ip-api.com/json/{aufsaifs}")
    if daaataaa.status_code == 200:
            boobaas = curl = daaataaa.json()
            print(boobaas)



