## OOPActPartII
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



