
from gtts import gTTS
import winsound


mytext = input()

language = 'en'


myobj = gTTS(text=mytext, lang=language, slow=False)


myobj.save("welcome.wav")

winsound.PlaySound("welcome.wav",winsound.SND_ASYNC)
