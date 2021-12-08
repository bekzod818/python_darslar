# Import the required module for text 
# to speech conversion
from gtts import gTTS
  
# This module is imported so that we can 
# play the converted audio
import os
  
# The text that you want to convert to audio
mytext = "«Президенты ознакомились с созданными в посольстве условиями. Современное здание возведено строителями нашей страны. Помещения оформлены в национальном стиле», - говорится в сообщении. На территории дипломатического представительства расположены основное здание, консульский отдел, жилой дом для сотрудников, резиденция главы дипмиссии, детская и спортивная площадки. В переговорных комнатах, конференц-зале созданы современные условия."
  
# Language in which you want to convert
language = 'ru'
  
# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)
  
# Saving the converted audio in a mp3 file named
# welcome 
myobj.save("welcome.mp3")
  
# Playing the converted file
os.system("mpg321 welcome.mp3")








# def synthesize_text(text):
#     """Synthesizes speech from the input string of text."""
#     from google.cloud import texttospeech

#     client = texttospeech.TextToSpeechClient()

#     input_text = texttospeech.SynthesisInput(text=text)

#     # Note: the voice can also be specified by name.
#     # Names of voices can be retrieved with client.list_voices().
#     voice = texttospeech.VoiceSelectionParams(
#         language_code="en-US",
#         name="en-US-Standard-C",
#         ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
#     )

#     audio_config = texttospeech.AudioConfig(
#         audio_encoding=texttospeech.AudioEncoding.MP3
#     )

#     response = client.synthesize_speech(
#         request={"input": input_text, "voice": voice, "audio_config": audio_config}
#     )

#     # The response's audio_content is binary.
#     with open("output.mp3", "wb") as out:
#         out.write(response.audio_content)
#         print('Audio content written to file "output.mp3"')

# s = "The Presidents got acquainted with the conditions created at the embassy. The modern building was erected by builders of our country. The premises are decorated in the national style, the report reads.There are the main building, the consular department, a residential building for employees, the residence of the head of the diplomatic mission, children’s and sports grounds on the territory of the diplomatic mission.Modern conditions have been created in the meeting rooms and conference hall."
# synthesize_text(s)