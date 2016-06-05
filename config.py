from pymongo import MongoClient
import os
from flask import Flask

application = Flask(__name__)

# try:
application.config.from_pyfile("dev_config.cfg")
application.config['SERVER'] = 'local server'
mc = MongoClient( application.config['MONGODB_URI'] )
db = mc.travelapplication

print(">>> Development configuration file loaded.")
# except:
#   #======================================
#   # Try to get amazon ec2 container tags
#   #======================================
#   pass
#   import boto.utils
#   import boto.ec2

#   iid_doc = boto.utils.get_instance_identity()['document']
#   region = iid_doc['region']
#   instance_id = iid_doc['instanceId']

#   ec2 = boto.ec2.connect_to_region(region)
#   instance = ec2.get_only_instances(instance_ids=[instance_id])[0]

#   tags = instance.tags

#   config = {}

#   config['DB_IP'] = tags['DB_IP']
#   config['MATRIX_API_KEY'] = [ tags['MATRIX_KEY'] ]
#   config['GEOCODER_API_KEY'] = tags['GEOCODER_KEY'].split(":")
#   config['EMAIL'] = { 'username' : tags['EMAIL_USER'], 'password' : tags['EMAIL_PASS'] }
#   config['DEBUG'] = tags['DEBUG'] == 'True'
#   config['SERVER'] = tags['elasticbeanstalk:environment-name']

#   application.config.update(config)
#   print '>>> Loaded amazon ec2 container tags'
#   print '[Current Configuration]\nDebug: %s\nServer: %s\nDB IP: %s' % (str(config['DEBUG']), config['SERVER'], config['DB_IP'])