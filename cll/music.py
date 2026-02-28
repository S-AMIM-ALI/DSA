#Design music playlist using CLL.
class song:
    def __init__(self,title=None,artist=None,next=None):
        self.title=title
        self.artist=artist
        self.next=next
class musicplaylist:
    def __init__(self,last=None,curr=None):
        self.last=last
        self.curr=curr
    def isempty(self):
        return self.last is None
    def add_song(self,title,artist):
        new_song=song(title,artist)
        if self.isempty():
            self.last=new_song
            new_song.next=new_song
        else:
            new_song.next=self.last.next
            self.last.next=new_song
            self.last=new_song
        print(f"song added is {title} by {artist}")
    def play_next(self):
        if self.isempty() :
            print("list is empty")
        elif self.curr is None:
            self.curr=self.last.next
        else:
            self.curr=self.curr.next
        print(f"now playing {self.curr.title} by {self.curr.artist}")
    def show_playlist(self):
        if self.isempty():
            return None
        else:
            curr=self.last.next
            while True:
                print(f"{curr.title} by {curr.artist}")
                if curr==self.last.next:
                    break
# Create playlist
playlist = musicplaylist()

# Add songs
playlist.add_song("Shape of You", "Ed Sheeran")
playlist.add_song("Blinding Lights", "The Weeknd")
playlist.add_song("Levitating", "Dua Lipa")
playlist.add_song("Bad Habits", "Ed Sheeran")

# Show playlist
playlist.show_playlist()

# Play songs in loop
for _ in range(6):  # play more than total songs to see looping
    playlist.play_next()
