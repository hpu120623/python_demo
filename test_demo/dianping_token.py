import base64, zlib, time

info = str({"rId":"","ts":int(time.time()*1000),"cts":int(time.time()*1000)+100,"brVD":[],"brR":[],"bI":[],"mT":[],"kT":[],"aT":[],"tT":[],"sign":"eJwDAAAAAAE="}).encode()
token = base64.b64encode(zlib.compress(info)).decode()
print(token)