import sys, json
import urllib.request as urllib2
weather_key = 'c14171b4eda5cd77c5267601811a2274'

current_weather_url = 'http://api.openweathermap.org/data/2.5/weather'

def getWeather(options):
    queryString = '&'.join(i['key']+'='+i['value'] for i in options)
    url = current_weather_url+'?'+queryString
    req = urllib2.Request(url)
    res = urllib2.urlopen(req).read().decode("utf-8")
    try:
        json_result = json.loads(res)['weather']
    except:
        print('Query failed')
        sys.exit(2)
    return json_result

def parseResultString(weatherObject):
    def returnWeatherDescription(i):
        return i['description']
    mapResult = list(map(returnWeatherDescription, weatherObject))
    resultsJoined = ', '.join(mapResult)
    return resultsJoined

def main(location):
    options = [{
        "key": "q",
        "value": location
    },{
        "key" : "APPID",
        "value": weather_key
    }]
    print ('Getting weather for '+location)
    resultJson = getWeather(options)
    parsedResult = parseResultString(resultJson)
    print("Current weather in "+location+" : "+parsedResult)

if __name__ == "__main__":
    try:
        location = sys.argv[1]
    except:
        print("Invalid Input")
        sys.exit(2)
    main(location)