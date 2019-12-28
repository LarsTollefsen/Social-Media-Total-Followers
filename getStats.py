import urllib.request
import json
import tweepy
import gspread
import os
from datetime import datetime
from oauth2client.service_account import ServiceAccountCredentials
from appJar import gui

##### EXPORT #####
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

credpath = os.path.dirname(os.path.abspath(__file__))
credpathname = credpath + "\creds.json"
creds = ServiceAccountCredentials.from_json_keyfile_name(credpathname, scope)

client = gspread.authorize(creds)

sheet = client.open("somestats").sheet1

##### FUNCTIONS #####
def makeGUI():
    global fb
    global total

    # Set global variables
    fb = int(app.getEntry("Facebook followers:"))
    total = yt + ig + fb + tv + t

    # Hide Facebook GUI buttons
    app.hideButton("Add Facebook followers")
    app.hideLabel("Facebook followers:")

    # Export button
    app.addButton("Export", exportToDrive, 2, 1)

    # YouTube
    app.startLabelFrame("YouTube", 0, 0)
    app.addImage("YouTube", "img/YouTube.gif")
    app.addLabel("YouTube", "Subscribers: " + str(yt))
    app.stopLabelFrame()

    # Instagram
    app.startLabelFrame("Instagram", 0, 1)
    app.addImage("Instagram", "img/Instagram.gif")
    app.addLabel("Instagram", "Followers: " + str(ig))
    app.stopLabelFrame()

    # Facebook
    app.startLabelFrame("Facebook", 0, 2)
    app.addImage("Facebook", "img/Facebook.gif")
    app.addLabel("Facebook", "Followers: " + str(fb))
    app.stopLabelFrame()

    #Twitch
    app.startLabelFrame("Twitch", 1, 0)
    app.addImage("Twitch", "img/Twitch.gif")
    app.addLabel("Twitch", "Followers: " + str(tv))
    app.stopLabelFrame()

    # Twitter
    app.startLabelFrame("Twitter", 1, 1)
    app.addImage("Twitter", "img/Twitter.gif")
    app.addLabel("Twitter", "Followers: " + str(t))
    app.stopLabelFrame()

    # Total
    app.startLabelFrame("Total", 1, 2)
    app.addImage("Total", "img/Total.gif")
    app.addLabel("Total", "Total: " + str(total))
    app.stopLabelFrame()


def exportToDrive():
    # Get date and time
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    #Insert data to the first data column in the sheet
    insertRow = [now, yt, fb, ig, tv, t, total]
    sheet.insert_row(insertRow, 2)

##### INIT #####
app = gui("Social Media Total Followers", "720x720")
app.setBg("white")
app.setFont(15)

##### FACEBOOK #####
app.addLabelEntry("Facebook followers:", 0, 0)
app.addButton("Add Facebook followers", makeGUI, 1, 0)

##### YOUTUBE #####
#YouTube API key
ytKey = ""
#YouTube Channel ID
ytID = ""                   

ytdata = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&id=" + ytID +"&key=" + ytKey).read()
ytjson = json.loads(ytdata)["items"][0]["statistics"]["subscriberCount"]
yt = int(ytjson)

##### INSTAGRAM #####
#Instagram username
igID = ""   

igdata = urllib.request.urlopen("https://www.instagram.com/" + igID + "/?__a=1").read()
ig = json.loads(igdata)["graphql"]["user"]["edge_followed_by"]["count"]

##### TWITCH #####
#Twitch Channel ID
tvID = ""
#Twitch API Key                        
tvKey = ""    

tvurl = urllib.request.Request("https://api.twitch.tv/helix/users/follows?to_id=" + tvID)
tvurl.add_header("Client-ID",tvKey)
tvdata = urllib.request.urlopen(tvurl).read()
tv = json.loads(tvdata)["total"]

##### TWITTER #####
# Twitter Consumer Key
tCK = ""
# Twitter Consumer Key Secret
tCKS = ""
# Twitter Access Token
tAT = ""
# Twitter Access Token Secret
tATS = ""
#Twitter username
tname = ""

tauth = tweepy.OAuthHandler(tCK, tCKS)
tauth.set_access_token(tAT, tATS)
tapi = tweepy.API(tauth)
t = tapi.get_user(tname).followers_count

##### RUN GUI #####
app.go()