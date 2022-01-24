import random
import time
import base64
import string
import os
import pythonping
import colorama
import discord
import requests
from os import system
from colorama import init, Fore, Style
from random import randint
from random import choice
from random import randrange
from pythonping import ping
from discord.ext import commands


system(f'title FreeMoneyHubs Multi Tool')
print(f"{Fore.RED}▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
print("▐                                         FreeMoneyHubs Multi Tool                                           ▐")
print("▐                                         ------------------------                                           ▐")
print("▐                                                                                                            ▐")
print("▐   1 = Card Gen   2 = Email Gen   5 = Phone Gen   7 = Nitro Gen                                             ▐")
print("▐                                                                                                            ▐")
print("▐   3 = Ip Pinger   4 = Ip Analyzer                                                                          ▐")
print("▐                                                                                                            ▐")
print("▐   6 = Discord Spammer                                                                                      ▐")
print("▐                                                                                                            ▐")
print("▐   8 = Base64 Encoder   9 = Base64 Decoder                                                                  ▐")
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
                print(f"{Fore.GREEN}{Style.BRIGHT}[!] Finished{Style.RESET_ALL}")

elif menu3 == '2':
    baiduj = input(f'{Fore.LIGHTBLUE_EX}[?] How Mail Emails To Make : ')
    with open(f"Emails{baiduj}.txt", "w", encoding='utf-8') as fileffs:
        jdjdjd = (['justin', 'james', 'juan', 'lopez', 'matt', 'bryan', 'tina', 'mark', 'mason', 'brass', 'jeff', 'caleb',
         'marten', 'willson', 'pro', 'old', 'oscar', 'asher', 'gaming', 'davis', 'noah', 'seth', 'trent', 'luke',
         'carson', 'ella', 'brook', 'tate', 'brice', 'collin', 'ryan','jamie','mega','ted','steve','joe','copper'])
        bbsi = (['@gmail.com', '@yahoo.com', '@hotmail.com'])
        inny23 = int(baiduj)
        time.sleep(.5)
        for i in range(inny23):
            partt0 = randrange(1, 999)
            partt1 = (random.choice(jdjdjd))
            partt2 = (random.choice(bbsi))
            print(f'{Fore.GREEN}{Style.BRIGHT}({i}) - {partt1}{partt0}{partt2}{Style.RESET_ALL}')
            fileffs.write(f"{partt1}{partt0}{partt2} \n")
        with open(f"mails{baiduj}.txt") as filebb:
            for line in file.readlines():
                emaildie = line.strip("\n")
                print(f"{Fore.GREEN}{Style.BRIGHT}[!] Finished{Style.RESET_ALL}")
elif menu3 == '3':
    ippp = input(f"{Fore.LIGHTBLUE_EX}[?] Enter Ip To Ping : ")
    ammo3unt = input(f"{Fore.LIGHTBLUE_EX}[?] Amount Of Times To Ping : ")
    nummies = int(ammo3unt)
    try:
        ping(f'{ippp}', count=nummies, verbose=True)
        time.sleep(1)
        print("[!] Finished")
    except:
        print(f"{Fore.RED}{Style.BRIGHT}[!] That Ip Is Not Possible To Even Have Retard{Style.RESET_ALL}")
elif menu3 == '4':
    aufsaifs = input(f"{Fore.LIGHTBLUE_EX}[?] Enter The Ip You Want To Get Info On : ")
    daaataaa = requests.get(f"http://ip-api.com/json/{aufsaifs}")
    if daaataaa.status_code == 200:
            boobaas = curl = daaataaa.json()
            print(boobaas)
elif menu3 == '5':
    phonee = input(f"{Fore.LIGHTBLUE_EX}[?] How Many Numbers To Generate : ")
    print(f"[!]{Fore.RED}  WE ONLY HAVE 250 REQ PER MONTH PER API KEY SO DONT FUCKING AFK THIS SHIT BRO")
    time.sleep(1)
    phonee2 = int(phonee)
    with open(f"PhoneNums{phonee2}.txt", "w", encoding='utf-8') as ggas:
        for i in range(phonee2):
            kyyee = random.choice(['8a9b286db37242278c650f057e69af0a','c18e40093aa54050869e6c025cd212ad','ce7e22fa1b664e30b7479c2fae835b6e','65fb967dd10d4dfdae57aac38359b784','4ef2dc40a978468fa34d3148fa5edea2','57e32fc3db4a43f8bb1a8789530e47e2','7dca8166ab2c4dac8fe6f92b4cbd6d07','fcdad5e099284c5b8e87a92a1ea799b8','a73831d44e694faaac2f2700cf477200','7da18e005724444fbc5c663b5f936bae','39d2d11cc1dc4e43a0f6d2851365fc74','1040025afab84d3fb0a54b03dc05e973','e366c837dfff41b6a929ea9c5dc39f39','e1cbb145d55c47beb794d53e0ecfd0e5','9349b70a50f94a08b33622c794f0133b','2baaaa8e8eab4a08aeea4fad3c5022eb','7c1e7070816f40a68f43c96a098e6247','82e2b664b70844beb297ade47f46bdf0'])
            areacodde = randrange(200, 999)
            telprefix = randrange(200, 999)
            linenumm = randrange(1000, 9999)
            sexa2 = print(f"{Fore.LIGHTGREEN_EX}({i}) Genned : 1-{areacodde}-{telprefix}-{linenumm}")
            sexa4 = (f" 1-{areacodde}-{telprefix}-{linenumm}")
            sexa3main = f"1{areacodde}{telprefix}{linenumm}"
            response = requests.get(f"https://phonevalidation.abstractapi.com/v1/?api_key={kyyee}&phone={sexa3main}")
            if response.status_code == 200:
                ggas.write(f"{sexa4}   -   {response.content} \n")
                print(f"{Fore.GREEN}Response For {sexa3main} - {response.content}")

            else:
                print(f"{Fore.RED}{Style.BRIGHT}[!] 404 NIGGA THIS API KEY GOT FUCKED WAIT 1 MONTH{Style.RESET_ALL}")
elif menu3 == '6':
    tooooken = input(f"{Fore.LIGHTBLUE_EX}[?] Enter Discord Token : ")
    print(f'Using {tooooken}')
    bot = commands.Bot(command_prefix='!')

    aaa3894 = input(f"{Fore.LIGHTBLUE_EX}[?]How Many Times Do Want To Spam : ")
    ghajfuj = input(f"{Fore.LIGHTBLUE_EX}[?] What Message Do You Want To Spam : ")
    G4dah4 = int(aaa3894)
    time.sleep(1)
    print(f"{Fore.LIGHTBLUE_EX}[!] Type - !spam Where You Want To Spam")
    time.sleep(1)
    @bot.event
    async def on_message(message):
        if message.content.startswith('!spam'):
            for i in range(G4dah4):
                await message.channel.send(f"({i}) {ghajfuj}")

    bot.run(f"{tooooken}", bot=False)
elif menu3 == '7':
    print(f"{Fore.RED}Due To The Shitty Chances Of Getting A Real Code We Dont Have A Checker Sorry")
    time.sleep(1)
    AMMOun4t = input(f"{Fore.LIGHTBLUE_EX}[?] How Many Codes Do You Want To Make : ")
    G4dah4ss = int(AMMOun4t)
    with open(f"NitroCodes{AMMOun4t}.txt", "w", encoding='utf-8') as fileffs:
        codeLen = 16
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        for i in range(G4dah4ss):
            cood43 = "".join(random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890") for _ in range(16))
            print(f"{Fore.GREEN}({i})discord.gift/{cood43}")
            fileffs.write(f"discord.gift/{cood43} \n")
elif menu3 == '8':
    messag3dea = input(f"{Fore.LIGHTBLUE_EX}[?] Type The Message You Want To Encode : ")
    sample_string = f"{messag3dea}"
    sample_string_bytes = sample_string.encode("ascii")
    base64_bytes = base64.b64encode(sample_string_bytes)
    base64_string = base64_bytes.decode("ascii")
    print(f"{Fore.GREEN}Encrypted Message : {base64_string}")
elif menu3 == '9':
    messag3desa = input(f"{Fore.LIGHTBLUE_EX}[?] Type The Message You Want To Decode : ")
    base64_string = f"{messag3desa}"
    base64_bytes = base64_string.encode("ascii")
    sample_string_bytes = base64.b64decode(base64_bytes)
    sample_string = sample_string_bytes.decode("ascii")
    print(f"{Fore.GREEN}Decrypted Message : {sample_string}")
















