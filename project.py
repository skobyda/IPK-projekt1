import sys
import socket
import json

if len(sys.argv) == 3:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("api.openweathermap.org", 80))
    client.send("GET /data/2.5/weather?q={0}&appid={1}&units=metric HTTP/1.1\r\nHost:api.openweathermap.org\r\n\r\n".format(sys.argv[2], sys.argv[1]).encode())
    response = client.recv(4096)
    response = response[response.find("{"):]

    dzejsn = json.loads(response)

    print(dzejsn["name"])
    print(dzejsn["weather"][0]["description"])
    print("temp:{0}C".format(dzejsn["main"]["temp"]))
    print("humidity:{0}%".format(dzejsn["main"]["humidity"]))
    print("pressure:{0} hPa".format(dzejsn["main"]["pressure"]))
    print("wind-speed: {0}km/h".format(dzejsn["wind"]["speed"]))
    print("wind-deg: {0}".format(dzejsn["wind"]["deg"]))
