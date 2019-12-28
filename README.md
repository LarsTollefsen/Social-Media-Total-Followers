# Social-Media-Total-Followers
Gets the total social media followers count from YouTube, Instagram, Facebook, Twitch and Twitter using Python. Small, quick and simple project to have the total stats more readily available. Does not use the Facebook API, but instead a manual input for the followers, since the API will only give out total likes and not followers. Export function connects to a spreadsheet and inserts the row into the first row with date, time and all the statistics.

This is meant to be a small start you can use if this is needed for a similar project, or if you just want to see the way I've done this if you're interested in re-creating this yourself. A great way to learn how to use APIs and how to get their statistics down into a variable.

## Getting Started

Clone (or download) the project. It's important that you do not change the folder structure without changing it in the code as well. 

If working with the APIs is confusing or new, be sure to check out YouTube with "Python" + the api you want to learn to use. Working with and getting these stats or other stats are pretty much the same, so if you're unsure, check out some tutorials on the topic.

### Prerequisites

Use pip to install the missing libraries used in the project(ex. Tweepy). See the import list and what you're missing.

## The different parts and how to make them work

I will now list the different sections that's been divided with comments with instructions of what needs changing when needed. Use this as both an explanation of the script and documentation. Decided to do it this way because of the simplicity and size of the script.

### EXPORT

The export section is simply creating the connection to a specified google drive spreadsheet by authorizing using a JSON file with credentials. It then opens a named sheet that the user in the credentials have been given edit access to. For more information on how to setup this step, feel free to follow this video:
https://www.youtube.com/watch?v=cnPlKLEGR7E

One thing to note is that I've had to use os.path.dirname to find the path for the script, then create a path variable by adding \creds.json on top. This is done because for some reason using a relative path gave out a "FileNotFoundError". Silly workaround.

### FUNCTIONS
#### makeGUI()
This is the function that creates the GUI using appjar from the data provided from the API sources and the input for the Facebook step. 
Two global variables are defined then given values to make them easily accessible by the exportToDrive function.

The different GUI elements are created inside some LabelFrame elements and the int values are converted into strings so they can be displayed. The .gif image format is used only because it's what is preferred by Appjar as it loads faster. Feel free to use .png if you want slower loading times.

#### exportToDrive()

Simply gets the system date and time with the format DAY/MONTH/YEAR HOUR/MINUTE/SECOND.
This is inserted into the insertRow array, which is then inserted into row two of my spreadsheet. The important part here is that I'm using insert_row, which pushes the new row in to the second row and all the other rows down. This doesn't delete previous exports and keeps track of every other export nicely.

### INIT
Small Appjar settings for the app window is set here.

### FACEBOOK
Creates an entry label and a button. Once the button is triggered these are removed by the makeGUI() function explained above.

### YOUTUBE

Uses the YouTube API to access channel statistics of a channel with a certain ID. Adds the "subscriberCount" to the yt variable and makes it an int.

### INSTAGRAM

Uses a simple url that is open. No need to for any API keys or page ID to get the statistics of the profile. 

### TWITCH

Twitch API similar to the YouTube request. Needs the API key added in the header.

### TWITTER

Twitter API needs tweepy installed to handle the authorization, but other than that it's the same process as the others to get the data. Be aware that you need four keys here. You need to register and wait for your developer application to go through to be able to get all these 4 keys.

### RUN GUI

Appjar requirement to run the GUI. Duh.

## Developing it further

This could be automated to run every X-hours or days depending on the need, which means you could also just cut out the whole GUI part. The reason I've made a GUI part was partly because I wanted to test out appjar, but mostly since not everything is worth exporting. Especially if there have been little to no changes, but you just want to check. The whole GUI can be revamped or removed as it's just giving you the same statistics being exported anyways.

Another way to develop this further could be to have more statistics inside the application it self. You can easily access the previous export(s) if you want to with the same connection created earlier to show changes since the last export and/or how long ago it was. Very simple changes that could add more to a simple program like this. Explore this if you want to use it as a learning experience and working with APIs.
