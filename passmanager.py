import os
import random

username = message.author
curdir = os.getcwd()
path = os.path.join(curdir, username)
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