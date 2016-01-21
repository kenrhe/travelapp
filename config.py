from pymongo import MongoClient
import os
from flask import Flask

app = Flask(__name__)

CONFIG = os.environ

mc = MongoClient(CONFIG['DB_IP']);
db = mc.uphail 

matrix_api_key_list = CONFIG['MATRIX_API_KEY']

geocoder_api_key_list = CONFIG['GEOCODER_API_KEY']

email = CONFIG['EMAIL']

def customError(error, details):
  fromaddr = email['username']
  toaddrs  = email['username']
  msg = "500 error.\n"
  msg += "Here's some information:\n"
  msg += "Error: %s\n" % str(error)
  for k,v in details.iteritems():
    msg += "\n [%s] : %s \n" % (k, v)
  # Credentials (if needed)
  username = email['username']
  password = email['password']

  # The actual mail send
  server = smtplib.SMTP('smtp.gmail.com:587')
  server.starttls()
  server.login(username,password)
  server.sendmail(fromaddr, toaddrs, msg)
  server.quit()
  return True