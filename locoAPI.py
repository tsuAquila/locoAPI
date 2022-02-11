import requests
import json

streamerID = input("Enter the StreamerID: ")

def loco(streamerID):
  response = requests.post("https://wrapapi.com/use/tsuAquila/locoapi/streamers/0.0.7", json={
  "streamerName": streamerID,
  "wrapAPIKey": "Lwk29zg2OOVXF4nps448ObemSIfTUqtu"
  }).json()
  latency = requests.get('https://wrapapi.com/use/tsuAquila/locoapi/streamers/0.0.7')

  streamer = response["data"]["name"]
  followers = response["data"]["followersViews"][24]
  views = response["data"]["followersViews"][26]
  live = response["data"]["live"][0]
  live3 = live[0:21]
  
  if live3 == "livevideosleaderboard" :
    live1 = live[21:]
    
    if live1 != "This streamer isn’t live right nowCheck out the streamer’s top videos instead!" :
      live2 = join(live1.split("}")[:-1]) + "}"
      liveDict = json.loads(live2)
      liveStatus = True
      streamURL = liveDict['contentUrl']
      streamTitle = liveDict["name"]
      thumbnailURL = liveDict["thumbnailUrl"]
      streamDesc = liveDict['description']
      streamDateTime = liveDict['uploadDate']
      locoJSON = {
        "streamerID" : streamerID ,
        "streamerName" : streamer ,
        "followers" : followers ,
        "views" : views ,
        "liveStatus" : liveStatus ,
        "streamDetails" : {"streamURL" : streamURL , "streamTitle" : streamTitle , "thumbnailURL" : thumbnailURL , "streamDesc" : streamDesc , "streamDateTime" : streamDateTime }
      }

    else :
      liveStatus = False
      locoJSON = {
        "streamerID" : streamerID ,
        "streamerName" : streamer ,
        "followers" : followers ,
        "views" : views ,
        "liveStatus" : liveStatus
      }
  
  else :
    live1 = live[10:]
    
    if live1 != "This streamer isn’t live right nowCheck out the streamer’s top videos instead!" :
      live2 = "}".join(live1.split("}")[:-1]) + "}"
      liveDict = json.loads(live2)
      liveStatus = True
      streamURL = liveDict['contentUrl']
      streamTitle = liveDict["name"]
      thumbnailURL = liveDict["thumbnailUrl"]
      streamDesc = liveDict['description']
      streamDateTime = liveDict['uploadDate']
      locoJSON = {
        "streamerID" : streamerID ,
        "streamerName" : streamer ,
        "followers" : followers ,
        "views" : views ,
        "liveStatus" : liveStatus ,
        "streamDetails" : {"streamURL" : streamURL , "streamTitle" : streamTitle , "thumbnailURL" : thumbnailURL , "streamDesc" : streamDesc , "streamDateTime" : streamDateTime }
      }

    else :
      liveStatus = False
      locoJSON = {
        "streamerID" : streamerID ,
        "streamerName" : streamer ,
        "followers" : followers ,
        "views" : views ,
        "liveStatus" : liveStatus
      }

  return (locoJSON)

print(loco(streamerID))