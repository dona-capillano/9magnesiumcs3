class Songs:
    def __init__(self, title: str, genre: str, __private_artist: str, album: str ):
        self.title = title
        self.genre = genre
        self.__private_artist = __private_artist
        self.album = album
    def entertain(self) -> None:
        print(f"Now playing: {self.title} by {self.__private_artist}. Enjoy!!")
    def energize (self, energy_boost: int) -> str:
        return f"'{self.title}' is blasting at level {energy_boost}! "
    def trigger_memories(self) -> str:
        return f"listening to '{self.title}' brings back lost memories associated with the {self.album} album."
    def get_artist(self) -> str:
        return self.__private_artist
    def set_artist(self, new_artist: str) -> None:
        if new_artist.strip():
            self.__private_artist = new_artist
            print(f"Artiste name updated to '{self.__private_artist}' for song: {self.title}")
        else:
            print("Error!! Artist name shall not be empty.")

if __name__ == "__main__":
    song1 = Songs("Pushing It Down and Praying", "Indie pop", "Lizzy McALpine", "Older (and Wiser)")
    song2 = Songs("La La Lost You", "pop and R&B", "88rising and NIKI", "Head In The Clouds" )
    print("--- BEFORE ---")
    print(f"Object 1: {song1.title} | Artist: {song1.get_artist()} | Genre: {song1.genre} | Album: {song1.album}")
    print(f"Object 2: {song2.title} | Artist: {song2.get_artist()} | Genre: {song2.genre} | Album: {song2.album}")
    print()

    print("Performing action on Object 1 (updating artist)...")
    song1.set_artist("Lizzy McALpine, 88rising and NIKI")
    print()

    print("--- AFTER ---")
    print(f"Object 1: {song1.title} | Artist: {song1.get_artist()} | Genre: {song1.genre} | Album: {song1.album}")
    
# Implement the New Class
class LikedSongsFolder:
    def __init__(self, folder_name: str, date_created: str ): 
        self.folder_name = folder_name
        self.date_created = date_created
        self.song_list = []
    def add_song(self, song: Songs) -> None:
        self.song_list.append(song)
        print(f"Added '{song.title}' to '{self.folder_name}' folder.")
    def display_folder(self) ->None:
        print(f"Folder: {self.folder_name} (Created: {self.date_created})")
        if not self.song_list:
            print("Folder is empty.")
            return
        for index, song in enumerate(self.song_list, start=1):
            print(f"{index}. {song.title} | Artist: {song.get_artist()} | Genre: {song.genre} | Album: {song.album}")

if __name__ == "__main__":
    print("=== A. BEFORE RELATIONSHIP ===")
    my_folder = LikedSongsFolder("My Favorite Song", "2026,09,20")

    song1 = Songs("Pushing It Down and Praying", "Indie pop", "Lizzy McALpine", "Older (and Wiser)")
    song2 = Songs("La La Lost You", "pop and R&B", "88rising and NIKI", "Head In The Clouds" )

    print(f"Folder vreated: '{my_folder.folder_name}' with 0 songs.")
    print(f"Standalone Song 1: {song1.title} | Artist: {song1.get_artist()} | Genre: {song1.genre} | Album: {song1.album}")
    print(f"Standalone Song 2: {song2.title} | Artist: {song2.get_artist()} | Genre: {song2.genre} | Album: {song2.album}")

    print("\n=== B. BUILDING RELATIONSHIP ===")
    my_folder.add_song(song1)
    my_folder.add_song(song2)

    print("\n=== C. AFTER RELATIONSHIP ===")
    my_folder.display_folder()