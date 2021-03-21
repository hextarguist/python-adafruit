#python3
from termcolor import colored
from Adafruit_IO import RequestError, Client, Feed
ADAFRUIT_IO_USERNAME = 'Targuist'
ADAFRUIT_IO_KEY = '0f5344244d12416f91950d354f332e17'

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
print(colored('\n************ Create By Najmeddine ************\n', 'green'))
try:
    rrr = input(colored('Enter Your Feed : ','blue'))
    led1 = aio.feeds(rrr)
except RequestError: #doesn t exit create a new feed
    led1_feed = Feed(name='led1')
    led1_feed = aio.create_feed(led1_feed)
fat = input('Enter Your Etat ')
if fat == "1":
   print(colored(rrr+" it is on ", 'green'))
elif fat == "0":
   print(colored(rrr+" it is off", 'red'))

aio.send_data(led1.key, fat)

