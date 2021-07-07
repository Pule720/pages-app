from logging import exception
from tkinter import *
from pytube import YouTube
import hashlib
import pyfiglet 
from coolStuff import colourCode  #colourCode is a library that i developed

# for every string.pprint() statement just use a normal print f

# initializing colour code 
string = colourCode.beautifulPrint()

WELCOME = "EXCALIBUR"
DESCRIPTION = "--Your personal CLI file Installer--"

woo = pyfiglet.print_figlet(WELCOME)

string.pprint(DESCRIPTION, None, "info")


class Login():
    def isValid(self, name: str, password: str):
        # sha256 algorithm 
        users = {

            "Deadsec" : b'\x93j\x18\\\xaa\xa2f\xbb\x9c\xbe\x98\x1e\x9e\x05\xcbx\xcds+\x0b2\x80\xeb\x94D\x12\xbbo\x8f\x8f\x07\xaf'       
               
                }
        
        users_names = users.keys()

        passwordAsByte = bytes(password, 'utf-8')
        passwrdEncoded = hashlib.sha256(passwordAsByte)
        passwordDigested = passwrdEncoded.digest()

        for i in users_names:
            if (name == i and passwordDigested == users[name]):
                string.pprint("You have been logged in", None, "success")
                return True
            else:
                string.pprint("Something went wrong, You were not logged in...", None, "error")
                return False

   

class YouTubeFileDownloader():
    SAVE_PATH = "C:/Users/pulen/OneDrive/Desktop/youtubeVids"

    def downloadYoutubeFile(self, videoUrl: str):
        try:
            ytVideo = YouTube(videoUrl)
        except Exception as e:
            string.pprint(stringg=e, colourr=None, calll="error")
            
        print("\n")
        print("##########################- VIDEO DATA -#############################")
        try :
            print(f"Video Title : {ytVideo.title}")
            print(f"Video Thumbnail URL : {ytVideo.thumbnail_url}")
            print(f"Channel Url : {ytVideo.channel_url}")
            print(f"Video Author : {ytVideo.author}")
            print(f"Video Description : {ytVideo.description}")      
        except Exception as e:
            string.pprint(stringg=e, colourr=None, calll="error")

        print("######################################################################")

        try:
            ytVideo.streams.first().download(output_path=self.SAVE_PATH)
        except Exception as e:
            string.pprint(stringg=e, colourr=None, calll="error")

        string.pprint(stringg="The download is complete, enjoy!", colourr=None, calll="success")  




if __name__ == "__main__":

    usersName = str(input("Enter your user name : ")) 
    userPassword = str(input("Enter your password : "))

    login = Login()
    
    if login.isValid(name=usersName, password=userPassword) :

        download = YouTubeFileDownloader()
        try :
            url = str(input("Please enter a valid url : "))
        except Exception as e:
            string.pprint(stringg=e, colourr=None, calll="error")
        
        download.downloadYoutubeFile(videoUrl=url)
        
        
        

        

        
        



                


