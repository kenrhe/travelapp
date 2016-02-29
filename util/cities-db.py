from pymongo import MongoClient
import pymongo
import sys

def clean(word):
    return word.lower().strip().replace(' ', '-')

mc = MongoClient('ip address')
db = mc.travelapp

us_cities = open('us-cities-sample.csv').read()
lines = us_cities.split('\r')
print "len: " + str(len(lines))

test = True
#print info
for line in lines:
    info = line.split(',')
    print info
    if info[0] == 'id':
        continue
    city = clean(info[1])
    state_code = clean(info[3])
    state = clean(info[4])
    country_code = 'us'

    z = info[5].split(',')
    zip_codes = z if type(z) is list else [z]
    try:
        lat = float(info[7])
        lon = float(info[8])
    except ValueError:
        lat = 0.0
        lon = 0.0
    try:
        population = int(info[10])
    except ValueError:
        population = 0

    if (test):
        # print info
        print "name = %s" % city
        print "state code = %s" % state_code
        print "state = %s" % state
        print "zip = %s" % str(zip_codes)
        print "lat = %f" % lat
        print "lon = %f" % lon
        print "population = %i" % population
        print "############################"
    else:
        # try:
        # print info[6]
        query = 'us/'+info[3].lower()+'/'+info[0].lower()
        json = {
            'state_full' : info[3].lower(),
            'state_code' : info[2].lower(),
            'zip_codes' : info[4],
            'loc' : {
                'type' : 'Point',
                'coordinates' : [float(str(info[6])),float(str(info[7]))]
            },
            'population' : ((int)(info[9]))
        }
        #db.UPDATE_STUFF.update( query , { '$set' : update }, upsert=True )
        print 'created ' + info[0]
        # except:
        #     print "not valid"
    #count = count + 1