import urllib
import json
from urllib.request import urlopen

class dressMe():
    #int temp
    #int wind
    #str city
    #str state
    
    def getCity(self):
        #TODO: get input and format it.
        return "chicago"
    
    def getState(self):
        #TODO: get input and format it.
        return "IL"

    def getJSON(self):
        self.city = self.getCity()
        self.state = self.getState()
        f = urlopen('http://api.wunderground.com/api/e192200277f69c33/geolookup/conditions/q/' + state + '/' + city + '.json')
        json_string = f.read().decode('utf-8')
        parsed_json = json.loads(json_string)
        f.close()
        return parsed_json
        
    def getTemp(self): #find a way to pass in the json
        location = parsed_json['location']['city']
        temp_f = parsed_json['current_observation']['temp_f']
        

    def getClouds(self): #find a way to pass in the json 
        location = parsed_json['location']['city']
        clouds = parsed_json['current_observation']['weather']

    #SAMPLE:    
    def test1(self):
        city = "new_york"
        state = "ny"
        #print(city, state)
        f = urlopen('http://api.wunderground.com/api/e192200277f69c33/geolookup/conditions/q/' + state + '/' + city + '.json')
        json_string = f.read().decode('utf-8')
        parsed_json = json.loads(json_string)
        location = parsed_json['location']['city']
        temp_f = parsed_json['current_observation']['temp_f']
        print ("Current temperature in %s is: %s" % (location, temp_f))
        condition = parsed_json['current_observation']['weather']
        print ("Current weather in %s is: %s" % (location, condition))
        f.close()

    
