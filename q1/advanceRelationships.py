from operator import index
from turtle import title


class Songs:
    def __init__(self, title: str, artist: str, genre: str, album: str):
        self.title = title
        self.artist = artist
        self.genre = genre
        self.album = album

    def get_info(self) -> str:
        return f"'{self.title}' by {self.artist} | Album: {self.album} | Genre: {self.genre}"

# Child class 
class LiveSongs(Songs):
    def __init__(self, title: str, artist: str, genre: str, album: str, venue: str):
        super().__init__(title, artist, genre, album)
        self.venue = venue

    def get_info(self) -> str:
        base_info = super().get_info()
        return f"{base_info} [Live at {self.venue}]" 

class LikedSongsFolder:
    def __init__(self, folder_name: str): 
        self.folder_name = folder_name
        self.song_list = []

    def add_song(self, song: Songs):
        self.song_list.append(song)
        print(f"Added '{song.title}' to '{self.folder_name}' folder.")

    def display_folder(self):
        print(f"Folder: {self.folder_name}")
        if not self.song_list:
            print("Folder is empty.")
            return
        for song in self.song_list:
            print(f"- {song.get_info()}")

if __name__ == "__main__":
    song1 = Songs('Pusing It Down and Praying', 'Indie pop', 'Lizzy McALpine', 'Older (and Wiser)')
    song2 = LiveSongs('Pushing It Down and Praying', 'Indie pop', 'Lizzy McALpine', 'Older (and Wiser)', 'Madison Square Garden')

    my_folder = LikedSongsFolder("My Favorite Songs")
    my_folder.add_song(song1)
    my_folder.add_song(song2)

    my_folder.display_folder()