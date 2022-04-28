from tkinter.messagebox import NO
import uuid
from venv import create
from gtts import gTTS
import datamodel
import pathlib

#def get_text_data(*, text, lang):
    #check new or custom 



def create_custom_voice(text, lang):
    if lang is None:
        lang= "en"
    tts= gTTS(text= text, lang= lang)
    filename = str(uuid.uuid1()) + '.mp3'
    base_location = './backend/mp3data/'
    tts.save(base_location + filename)
    datamodel.insert_data(text.lower(), lang.lower(), filename, base_location)

#create_custom_voice("Manojkumar", "en")


def delete_custom_voice(text, lang):
    if lang is None:
        lang= "en"
    is_text_available = datamodel.delete_data(text.lower(), lang.lower()) 
    if is_text_available[0]:
        file_to_remove = pathlib.Path(is_text_available[2]+is_text_available[1])
        file_to_remove.unlink()

#delete_custom_voice("Manojkumar", "en")

def update_custom_voice(text, lang):
    if lang is None:
        lang = "en"
    filename = str(uuid.uuid1()) + '.mp3'
    base_location = './backend/mp3data/'
    datamodel.update_data(text.lower(), lang.lower(), filename, base_location)

update_custom_voice("Manojkumar", "en")
    