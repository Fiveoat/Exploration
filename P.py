from collections import deque


class Song:
    def __init__(self):
        self.title = ""
        self.artist = ""

    def prompt(self):
        self.title = input("Enter the title: ")
        self.artist = input("Enter the artist: ")

    def display(self):
        print(self.title + " by " + self.artist)


def main():
    playlist = deque()
    while True:
        song = Song()
        print("Options:")
        print("1. Add a new song to the end of the playlist")
        print("2. Insert a new song to the beginning of the playlist")
        print("3. Play the next song")
        print("4. Quit")
        choice = input("Enter Selection: ")
        print("")
        if choice == "1":
            song.prompt()
            playlist.append(song)
        elif choice == "2":
            song.prompt()
            playlist.appendleft(song)
        elif choice == "3":
            try:
                track = playlist.popleft()
                print("Playing song: ")
                track.display()
            except IndexError:
                print("The playlist is currently empty.")
                continue
        elif choice == "4":
            print("Goodbye")
            break
        print("")


if __name__ == '__main__':
    main()
