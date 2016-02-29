from pymongo import MongoClient
import pymongo
import sys

mc = MongoClient('ip address')
db = mc.travelapp

us_cities = open('us-cities-sample.csv').read()
lines = us_cities.split('\r')
print "len: " + str(len(lines))

test = True
#print info
for line in lines:
    info = line.split(',')
    city = info[1]
    state_code = info[2]
    state = info[3]
    country_code = 'us'

    zip_codes = info[4].split(',')
    lat = info[6]
    lon = info[7]
    
    population = info[9]
    if (test):
        print info
        # print "name = " + city
        # print "state code = " + state_code
        # print "state = " + state
        # print "zip = " + zip_codes
        # print "lat = " + lat
        # print "lon = " + lon
        # print "population = " + population
        # print "############################"
    else:
        # try:
        print info[6]
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