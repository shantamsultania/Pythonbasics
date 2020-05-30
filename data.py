from gtts import gTTS
import os
from googletrans import Translator

# first enter data

disease_id = list(range(9))
disease_name = [' Tomato___Bacterial_spot','Tomato___Early_blight','Tomato___Late_blight'
    ,'Tomato___Leaf_Mold','Tomato___Septoria_leaf_spot',
                'Tomato___Spider_mites','Two-spotted_spider_mite',
                'Tomato___Target_Spot','Tomato___Tomato_mosaic_virus ','Tomato___Tomato_Yellow_Leaf_Curl_Virus']
disease = 'dummy'
how = 'dummy'
identify = 'dummy'
what = 'dummy'
cultural_control = 'dummy'
chemical_control = 'dummy'
bio_control = 'dummy'
weed_report = 'dummy'
pest_report = 'dummy'
costing = 'dummy'
suggestion = 'dummy'
gov_sh = 'dummy'

data = [disease,how,identify,what,cultural_control,chemical_control,bio_control,weed_report,pest_report
    ,costing,suggestion,gov_sh]

# cost rate conversion in various units

# get choice for translator


lang2 = ['bengali', 'hindi', 'english', 'gujrati', 'Kannada', 'Malayalam', 'tamil', 'telugu', 'arabic']
input_choice = 2

def get_choice(input_choice):
    lang1 = ['bn', 'hi', 'en', 'gu', 'kn', 'ml', 'ta', 'te', 'ar']
    choice = lang1[input_choice]
    return choice

user_choice = get_choice(input_choice)
# translator
file = open('data.txt', 'w')
def translator(data,choice):
    translator = Translator()
    text_translated = translator.translate(data, src='en', dest=choice)
    print(text_translated.text)
    return text_translated.text

write_data = translator(data)

# save in mp4, pdf, txt, word
file.close()

# txt to speech save
myobj = gTTS(text=write_data, lang=user_choice, slow=False)

# playing the data speech
play_Data = True
if play_Data is True:
    myobj.save("data.mp3")
    os.system("welcome.mp3")
else:
    myobj.save("data.mp3")
    print('you can also listen ti the report it has been saved in your language')