import urllib.request, urllib.parse, urllib.error
import json



googleurl = "https://maps.googleapis.com/maps/api/geocode/json?"

while True:


    input = input("Enter a location: ")

    if len(input)<1: break

    url = googleurl + urllib.parse.urlencode( {"address": input})

    print("Retriveing",url)

    request = urllib.request.urlopen(url)
    data = request.read().decode()

    print("Retrieved",len(data),"characters")

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status']!='OK':
        print(data)
        continue


    print(json.dumps(js,indent=4))

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']

    print('lat',lat,'lng',lng)
