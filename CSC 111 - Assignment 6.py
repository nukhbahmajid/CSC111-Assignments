# ----------------------------------------------------------------------------------
#        Name: Nukhbah Majid (I did not collaborate with anybody on this assignment
#    Filename: CSC 111 - Assignment 6
#        Date: 10/19/18
# Description: Compiling a music library with certain functions like adding songs,
#              removing songs, playing songs, printing the contents of the library,
#              and quitting the music library. 
# ----------------------------------------------------------------------------------

import webbrowser

def printML(music_library):
    for i in range(len(music_library)):
        print("")
        print(str(i + 1) + ".", "'" + music_library[i]["Song Title"] + "'", "by", music_library[i]["Artist"], "(" + music_library[i]["Album"] + ")" )
        
def removeML(music_library):
    print("")
    userSongNo = int(input("Which song number would you like to remove?: "))
    music_library.pop(userSongNo - 1)
    print("Removing Song Number", str(userSongNo) + ":", "Done!")


def playML(music_library):
    print("")
    userSongNo = int(input("Which song # would you like to play?: "))
    print("Now playing Song number:", userSongNo)
    userSongNo = userSongNo - 1
    webbrowser.open(music_library[userSongNo]["Spotify URL"])
    

def main():
    
    print("""
    .___  ___.  __    __       _______. __    ______     __       __  .______   .______          ___      .______     ____    ____    
    |   \/   | |  |  |  |     /       ||  |  /      |   |  |     |  | |   _  \  |   _  \        /   \     |   _  \    \   \  /   /    
    |  \  /  | |  |  |  |    |   (----`|  | |  ,----'   |  |     |  | |  |_)  | |  |_)  |      /  ^  \    |  |_)  |    \   \/   /     
    |  |\/|  | |  |  |  |     \   \    |  | |  |        |  |     |  | |   _  <  |      /      /  /_\  \   |      /      \_    _/      
    |  |  |  | |  `--'  | .----)   |   |  | |  `----.   |  `----.|  | |  |_)  | |  |\  \----./  _____  \  |  |\  \----.   |  |        
    |__|  |__|  \______/  |_______/    |__|  \______|   |_______||__| |______/  | _| `._____/__/     \__\ | _| `._____|   |__|        
                                                                                                                                      
     
    """)

    print("")
    music_library = []
    user_option = input("Select an option (ADD, REMOVE, PRINT, PLAY, QUIT): ")
    user_option = user_option.upper()

    while (user_option != "QUIT"):
        
        if (user_option == "ADD"):
            print("")
            song = input("Song Title: ")
            artist = input("Artist: ")
            album = input("Album: ")
            spotify_link = input("Spotify URL: ")
            print("")
            song_info = {"Song Title":song, "Artist":artist, "Album":album, "Spotify URL":spotify_link}
            music_library.append(song_info)
            user_option = input("Select an option (ADD, REMOVE, PRINT, PLAY, QUIT): ")
            user_option = user_option.upper()

        elif (user_option == "PRINT"):
            print_musicLibrary = printML(music_library)
            print("")
            user_option = input("Select an option (ADD, REMOVE, PRINT, PLAY, QUIT): ")
            user_option = user_option.upper()


        elif (user_option == "REMOVE"):
            remove_musicLibrary = removeML(music_library)
            print("")
            user_option = input("Select an option (ADD, REMOVE, PRINT, PLAY, QUIT): ")
            user_option = user_option.upper()
 

        elif (user_option == "PLAY"):
            play_musicLibrary = playML(music_library)
            print("")
            user_option = input("Select an option (ADD, REMOVE, PRINT, PLAY, QUIT): ")
            user_option = user_option.upper()


        else:
            print("")
            user_option = input("Invalid function! Please pick an option (ADD, REMOVE, PRINT, PLAY, QUIT): ")
            user_option = user_option.upper()


    while (user_option == "QUIT"):
        print("")
        print("Goodbye!")
        break

            
              
            


if __name__ == ("__main__"):
    main()




#--------------------------------------------------------------------------------------------------------------
# References: Got help from the lab instructions for the play function (how to import webbrowser and open URL) |
#--------------------------------------------------------------------------------------------------------------
