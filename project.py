import sys
import socket
import json

if len(sys.argv) == 3:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock.connect(("api.openweathermap.org", 80))
    except:
        print("Could not connect to api.openweathermap.org")
        sock.close()
        sys.exit(1)

    try:
        sock.send("GET /data/2.5/weather?q={0}&appid={1}&units=metric HTTP/1.1\r\nHost:api.openweathermap.org\r\n\r\n".format(sys.argv[2], sys.argv[1]).encode())
        response = sock.recv(4096)
    except InterruptedError:
        print("System call was interrupted")
        sock.close()
        sys.exit(1)

    sock.close()

    if not response.startswith("HTTP/1.1 200 OK"):
        print("Received incorrect response from HTTP request (Expected HTTP/1.1 200 OK)")
        sys.exit(1)

    response = response[response.find("{"):] # remove everything before {, so only JSON remains

    dzejsn = json.loads(response)

    # Some property (like wind-deg) might not exist. So if it's not in json object, just ignore printing it
    # Kinda hacky
    try:
        print(dzejsn["name"])
    except KeyError:
        pass
    try:
        print(dzejsn["weather"][0]["description"])
    except KeyError:
        pass
    try:
        print("temp:{0}'\u00B0'C".format(dzejsn["main"]["temp"]))
    except KeyError:
        pass
    try:
        print("humidity:{0}%".format(dzejsn["main"]["humidity"]))
    except KeyError:
        pass
    try:
        print("pressure:{0} hPa".format(dzejsn["main"]["pressure"]))
    except KeyError:
        pass
    try:
        print("wind-speed: {0}km/h".format(float(dzejsn["wind"]["speed"]) * 3.6)) #convert m/s to km/h
    except KeyError:
        pass
    try:
        print("wind-deg: {0}".format(dzejsn["wind"]["deg"]))
    except KeyError:
        pass
