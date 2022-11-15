import discord
import string
import random
import os

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
