from pymongo import MongoClient

# pprint will make it prettier
from pprint import pprint

# connection go localhost MongoDB
client = MongoClient("localhost")
db=client.admin

# Issue the serverStatus and print it
serverStatusResult=db.command("serverStatus")
print(serverStatusResult, file=open("serverStatus.txt", "a"))