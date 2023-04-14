import board
import audiomp3
import audioio
# import audiocore
import audiomixer
import digitalio
import displayio
import time
import keypad
import neopixel
import terminalio
from adafruit_display_text import bitmap_label

# Color constants
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
BLACK = (0, 0 ,0)
RAINBOW = [
    RED, YELLOW, GREEN, BLUE, PURPLE
]

class WordCloud:

    text = (
        'hourqworkxis', # 0
        'makesgvusrdo', # 1
        'itbnstronger', # 2
        'afterpharder', # 3
        'betterwymore', # 4
        'thanlxtnever', # 5
        'fasterclover', # 6
    )

    positions = { # row, columns
        "after": (3, 0),
        "better": (4, 0),
        "do": (1, 10),
        "ever": (5, 8),
        "faster": (6, 0),
        "harder": (3, 6),
        "hour": (0, 0),
        "is": (0, 10),
        "it": (2, 0),
        "make": (1, 0),
        "makes": (1, 0),
        "more": (4, 8),
        "never": (5, 7),
        "over": (6, 8),
        "stronger": (2, 4),
        "than": (5, 0),
        "us": (1, 7),
        "work": (0, 5),
    }

    cues = (
        (  50, ), # this starts word clock display
        (  51.385181, "work", "it" ),
        (  52.376193, "make", "it" ),
        (  53.396700, "do", "it" ),
        (  54.299229, "makes", "us" ),
        (  55.083781, ),
        (  59.667214, "harder" ),
        (  60.670024, "better" ),
        (  61.383789, "faster" ),
        (  62.569465, "stronger" ),
        (  63.097415, ),
        (  66.937589, "more", "than"),
        (  67.925652, "hour" ),
        (  68.739698, "hour", "never" ),
        (  70.568648, ),
        (  75.260915, "ever" ),
        (  76.195888, "after" ),
        (  77.151507, "work", "is" ),
        (  78.127772, "over" ),
        (  78.820441, ),
        (  82.501795, "work", "it" ),
        (  83.451515, "make", "it" ),
        (  84.457275, "do", "it" ),
        (  85.398147, "makes", "us" ),
        (  86.383261, ),
        (  90.807424, "harder" ),
        (  91.763043, "better" ),
        (  92.485657, "faster" ),
        (  93.641838, "stronger" ),
        (  94.449985, ),
        (  98.060102, "work", "it" ),
        (  98.676536, "harder" ),
        (  99.048165, "make", "it" ),
        (  99.540722, "better" ),
        ( 100.033279, "do", "it" ),
        ( 100.541215, "faster" ),
        ( 100.997747, "makes", "us" ),
        ( 101.493253, "stronger" ),
        ( 101.979911, ),
        ( 105.852528, "more", "than", "ever" ),
        ( 106.893681, "hour", "after" ),
        ( 107.940733, "hour" ),
        ( 108.390620, "work", "is", "never", "over" ),
        ( 109.899000, ),
        ( 113.612510, "work", "it", "harder" ),
        ( 114.700946, "make", "it", "better" ),
        ( 115.658769, "do", "it", "faster" ),
        ( 116.647486, "makes", "us", "stronger" ),
        ( 117.641448, "more", "than", "ever" ),
        ( 118.584759, "hour", "after" ),
        ( 119.499045, "hour" ),
        ( 120.006981, "work", "is", "never", "over" ),
        ( 121.431482, "work", "it", "harder" ),
        ( 122.345767, "make", "it", "better" ),
        ( 123.434203, "do", "it", "faster" ),
        ( 124.342581, "makes", "us", "stronger" ),
        ( 125.401431, "more", "than", "ever" ),
        ( 126.274465, "hour", "after" ),
        ( 127.348062, "hour" ),
        ( 127.710844, "work", "is", "never", "over" ),
        ( 129.194413, "work", "it", "harder" ),
        ( 130.132336, "make", "it", "better" ),
        ( 131.278821, "do", "it", "faster" ),
        ( 132.238237, "makes", "us", "stronger" ),
        ( 133.182059, "more", "than", "ever" ),
        ( 133.987257, "hour", "after" ),
        ( 134.990067, "hour" ),
        ( 135.585078, "work", "is", "never", "over" ),
        ( 136.963244, "work", "it", "harder" ),
        ( 137.936560, "make", "it", "better" ),
        ( 138.908895, "do", "it", "faster" ),
        ( 139.874343, "makes", "us", "stronger" ),
        ( 140.841760, "more", "than", "ever" ),
        ( 141.812127, "hour", "after" ),
        ( 142.817886, "hour", "work", "is", "never", "over" ),
        ( 144.743872, "work", "it", "harder" ),
        ( 145.708340, "make", "it", "better" ),
        ( 146.719998, "do", "it", "faster" ),
        ( 147.649073, "makes", "us" ),
        ( 148.348386, ),
        ( 152.023095, "never", "over" ),
        ( 152.492056, "work", "it", "harder" ),
        ( 153.488968, "make", "it", "better" ),
        ( 154.453435, "do", "it", "faster" ),
        ( 155.181948, "makes", "us", "stronger" ),
        ( 156.520994, ),
        ( 158.480178, "hour" ),
        ( 158.886527, "work", "is", "never", "over" ),
        ( 160.381312, ),
        ( 182.765130, "never", "over" ),
        ( 183.585075, "work", "it" ),
        ( 184.573138, "make", "it", "better" ),
        ( 185.664432, "do", "it", "faster" ),
        ( 186.564205, "makes", "us", "stronger" ),
        ( 187.528479, "more", "than", "ever" ),
        ( 188.457278, "hour", "after" ),
        ( 189.436768, ),
        ( 191.442389, "work", "it" ),
        ( 191.831715, ),
        ( 193.185509, "do", "it" ),
        ( 193.867596, ),
        ( 197.942960, "work", "is", "never", "over" ),
        ( 199.128036, ),
        ( 206.896867, "work", "it", "harder" ),
        ( 208.858246, "do", "it", "faster" ),
        ( 210.819625, "more", "than", "ever" ),
        ( 212.754459, "hour" ),
        ( 213.224019, "work", "is", "never", "over" ),
        ( 214.704040, "work", "it", "harder" ),
        ( 215.683255, "make", "it", "better" ),
        ( 216.783397, "do", "it", "faster" ),
        ( 217.647583, "makes", "us", "stronger" ),
        ( 218.647444, "more", "than", "ever" ),
        ( 219.474655, "hour", "after" ),
        ( 220.546885, "hour" ),
        ( 220.871923, "work", "is", "never", "over" ),
        ( 222.561354, ),
        ( 999, ),
    )

    def __init__(self):
        self.display = board.DISPLAY
        # self.group = displayio.Group(x=160//4, y=120//4)
        self.group = displayio.Group(scale=2)
        for i in range(0, 7):
            row_label = bitmap_label.Label(terminalio.FONT, text=self.text[i], color=0x444444)
            row_label.x = 4
            row_label.y = 4 + 9 * i
            self.group.append(row_label)

        self.highlight_labels = {}
        for word in self.positions:
            pos = self.positions[word]
            highlight_label = bitmap_label.Label(terminalio.FONT, text=word, color=0xFFFFFF)
            highlight_label.x = 4 + pos[1] * 6
            highlight_label.y = 4 + 9 * pos[0]
            self.highlight_labels[word] = highlight_label

        self.reset()

    def reset(self):
        self.next_cue = 0

    def present(self, current_time):
        if current_time > self.cues[self.next_cue][0]:
            cue = self.cues[self.next_cue]
            self.next_cue += 1

            while len(self.group) > 7:
                self.group.pop()

            # add overdraws for highlighted words
            for i in range(1, len(cue)):
                self.group.append(self.highlight_labels[cue[i]])

            self.display.show(self.group)
            self.display.refresh()

    def active(self, current_time):
        # not active before first real cue is played
        if self.next_cue < 1:
            return False

        # we are active if we're showing text
        current_cue = self.cues[self.next_cue - 1]
        return len(current_cue) > 1


class DaftPunkLogo:

    def __init__(self):
        self.display = board.DISPLAY
        self.group = displayio.Group()
        daft_punk_logo = displayio.OnDiskBitmap("daftpunk_160x128.bmp")
        face = displayio.TileGrid(daft_punk_logo, pixel_shader=daft_punk_logo.pixel_shader)
        self.group.append(face)

    def show(self):
        self.display.show(self.group)
        self.display.refresh()


# start main code

keys = keypad.ShiftRegisterKeys(
        clock=board.BUTTON_CLOCK,
        data=board.BUTTON_OUT,
        latch=board.BUTTON_LATCH,
        key_count=8,
        value_when_pressed=True,
    )

board.DISPLAY.brightness = 0.8
board.DISPLAY.auto_refresh = False
speaker_enable = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
a = audioio.AudioOut(board.A0)
data = open("Harder Better Faster Stronger.mp3", "rb")
music = audiomp3.MP3Decoder(data)
mixer = audiomixer.Mixer(voice_count=1, sample_rate=44100, channel_count=1,
                         bits_per_sample=16, samples_signed=True, buffer_size=8192)
a.play(mixer)

neopixels = neopixel.NeoPixel(
    board.NEOPIXEL, 5, brightness=0.05, pixel_order=neopixel.GRB
)

wordcloud = WordCloud()
logo = DaftPunkLogo()

def setVUMeter(level): 
    for i in range(0, 5):
        if level > (i + 2) * 24:
            neopixels[i] = RAINBOW[i]
        else:
            neopixels[i] = BLACK
    neopixels.show()

while True:
    logo.show()
    # wait for a keypress before starting animation
    keys.events.clear()
    while True:
        key = keys.events.get()
        if key != None and key.released:
            break
        time.sleep(0.1)
    keys.events.clear()

    # Play the first sample voice
    speaker_enable.switch_to_output(value=True)
    mixer.voice[0].level = 0.1
    mixer.voice[0].play(music)
    show_vumeter = True
    while mixer.playing:
        if (key := keys.events.get()) != None and key.released:
            break

        # turn off VU meter once wordcloud appears
        position = music.samples_decoded / 44100
        wordcloud.present(position)
        if wordcloud.active(position):
            setVUMeter(0)
        else:
            setVUMeter(music.rms_level)

        time.sleep(0.05)

    mixer.stop_voice()
    speaker_enable.switch_to_output(value=False)
    setVUMeter(0)
    wordcloud.reset()
