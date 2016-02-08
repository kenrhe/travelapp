from pymongo import MongoClient
import os
from flask import Flask

application = Flask(__name__)

CONFIG = os.environ

# mc = MongoClient(CONFIG['DB_IP']);
# db = mc.uphail 

# matrix_api_key_list = CONFIG['MATRIX_API_KEY']

# geocoder_api_key_list = CONFIG['GEOCODER_API_KEY']

# email = CONFIG['EMAIL']