from i3pystatus import IntervalModule


class Pianobar(IntervalModule):
    """
    Shows the title and artist name of the current music

    In pianobar config file must be setted the fifo and event_command options
    (see man pianobar for more information)

    For the event_cmd use:
    https://github.com/jlucchese/pianobar/blob/master/contrib/pianobar-song-i3.sh

    Mouse events:
    - Left click play/pauses
    - Right click plays next song
    - Scroll up/down changes volume
    """

    settings = (
        ("format"),
        ("songfile", "File generated by pianobar eventcmd"),
        ("ctlfile", "Pianobar fifo file"),
        ("color", "The color of the text"),
    )
    format = "{songtitle} -- {songartist}"
    required = ("format", "songfile", "ctlfile")
    color = "#FFFFFF"

    on_leftclick = "playpause"
    on_rightclick = "next_song"
    on_upscroll = "increase_volume"
    on_downscroll = "decrease_volume"

    def run(self):
        with open(self.songfile, "r") as f:
            contents = f.readlines()

        sn = contents[0].strip()
        sa = contents[1].strip()

        self.output = {
            "full_text": self.format.format(songtitle=sn, songartist=sa),
            "color": self.color
        }

    def playpause(self):
        open(self.ctlfile, "w").write("p")

    def next_song(self):
        open(self.ctlfile, "w").write("n")

    def increase_volume(self):
        open(self.ctlfile, "w").write(")")

    def decrease_volume(self):
        open(self.ctlfile, "w").write("(")
