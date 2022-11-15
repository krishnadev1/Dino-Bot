import discord
import string
import random
import os
import requests
import csv

file = open('dataset.txt', 'r')
lst = file.read().splitlines()
dict = {}
for i in lst:
    s = i.split('=')
    dict[s[0]] = s[1]

print(dict)


async def command(message):
    username = str(message.author).split("#")[0]
    user_message = str(message.content)
    try:
        if not message.guild:
            try:
                await message.channel.send("This is a DM.")
                if user_message.lower() == 'generate password':
                    password = genpassword()
                    await message.channel.send(password)
                elif user_message.lower().__contains__('savepass'):
                    passmanager(username, user_message)
                    await message.channel.send('Password saved to our server')
                # elif user_message.lower().__contains__('dm'):
                #     await message.channel.send('Hello Buddy')
            except discord.errors.Forbidden:
                pass
        else:

            channel = str(message.channel.name)

            print(user_message)
            print(f'Message {user_message} by {username} on {channel}')
            # if message.author == :
            #     return

            if user_message.lower() == 'generate password':
                password = genpassword()
                await message.channel.send(password)

            elif user_message.lower().__contains__('savepass'):
                passmanager(username, user_message)
                await message.channel.send('Password saved to our server')
            elif user_message.lower().startswith("!stock"):
                company_name = user_message.split(" ")[1]
                stdetails = stock_price(company_name)
                await message.channel.send(stdetails)
            else:
                key = list(dict.keys())

                print(key)
                a = user_message.split(' ')

                for i in key:
                    if a[0] in i:
                        # if i.__contains__(user_message.lower()):
                        if a[0].__contains__('dm'):
                            await message.author.send('Hello Buddy')
                            await message.channel.send('Message sent.Go check your dm😉')
                        elif len(a) > 1 and a[1].lower() != 'dyno':
                            await message.channel.send(
                                f'Hello {username}. Just to remind you my name is Dyno and not {a[1]} 😒')

                        else:
                            await message.channel.send(dict[i])
    except discord.errors.Forbidden:
        pass


def genpassword():
    lenopass = random.randint(7, 11)
    S = lenopass
    ran = ''.join(random.choices(string.ascii_letters + string.digits, k=S))
    return "Hey Buddy. I just generated an awesome strong password for you. Your password is " + ran


def passmanager(username, user_message):
    # username = str(message.author)
    curdir = os.getcwd()
    print(curdir)

    path = os.path.join(curdir, username)
    print(path)
    # user_message=message.content()
    website = user_message.split(" ")[1]
    username = user_message.split(" ")[2]
    password = user_message.split(" ")[3]
    try:
        os.mkdir(path)
        file = open(path + '\\' + website + ".txt", "a+")
        file.writelines(username + ":" + password + "\n")
        file.close()
    except OSError as error:
        print("Folder already created")
        file = open(path + '\\' + website + ".txt", "a+")
        file.writelines(username + ":" + password + "\n")
        file.close()


def stock_price(company_name):
    try:
        CSV_URL2 = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol='
        CSV_URL = CSV_URL2 + company_name + "&interval=15min&slice=year1month1&apikey=4Q2E15KNNAHLJH6C"
        with requests.Session() as s:
            download = s.get(CSV_URL)
            decoded_content = download.content.decode('utf-8')
            cr = csv.reader(decoded_content.splitlines(), delimiter=',')
            my_list = list(cr)

        times = my_list[1][0]
        opens = my_list[1][1]
        highs = my_list[1][2]
        lows = my_list[1][3]
        closes = my_list[1][4]
        volumes = my_list[1][5]
        userout = "Company Name: " + company_name + "\n\n" + "Time " + times + "\n" + "Opening Price: " + opens + "\n" + "High: " + highs + "\n" + "Low: " + lows + "\n" + "Closing Price: " + closes + "\n" + "Volume Traded: " + volumes
    except:
        userout = "Sorry😪\nCurrently we only support stocks listed in the International Market. We will soon be adding others too.\n\nTry accessing the stock of AMAZON by the command !stock AMZN"
    return userout