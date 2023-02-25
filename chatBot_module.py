import speech_recognition as sr  # 匯入套件並命名為 sr
from gtts import gTTS
from pygame import mixer
from bs4 import BeautifulSoup
import re
import requests
import os
from hanziconv import HanziConv



mixer.init()
mixer.init() 
def bot_speak(text, lang):    
    try: 
        tts = gTTS(text=text, lang=lang)
        tts.save('speak.mp3')
        mixer.music.load('speak.mp3')
        mixer.music.play()    
        while(mixer.music.get_busy()):
            continue
    except:
        print('播放音效失敗')



def bot_listen():
    recong = sr.Recognizer()            
    with sr.Microphone() as source:     
        audioData = recong.listen(source)      
    try:
        text = recong.recognize_google(audioData, language='zh-tw')    
        return text
    except:
        return '聽不懂'


def bot_get_wiki(keyword):
    response = requests.get('https://zh.wikipedia.org/zh-tw/' + keyword)
    bs = BeautifulSoup(response.text, 'lxml')
    p_list = bs.find_all('p')
    for p in p_list:
        if keyword in p.text[0:10]:
            return p.text
        
        
        
def bot_speak_re(sentence):
    s1 = re.sub(r'\[[^\]]*\]', '', sentence)
    print(s1)
    en_list = re.findall(r'[a-zA-Z ]+' ,s1)
    s2 = re.sub(r'[a-zA-Z \-]+', '@english@', s1)
    all_list = s2.split('@')
    index = 0
    for text in all_list:
        if text != 'english':
            bot_speak(text, 'zh-tw')
        else:
            bot_speak(en_list[index], 'en')
            index += 1
        
        
def bot_get_google(question):
    url = f'https://www.google.com.tw/search?q={question}+維基百科'
    headers = {
        'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        bs = BeautifulSoup(response.text, 'lxml')
        wiki_url = bs.find('cite')
        print(wiki_url.text)
        #kwd = wiki_url.text.split('/')  
        kwd = wiki_url.text.split('›')[-1].replace(' ','')
        keyword_trad = HanziConv.toTraditional(kwd)
        return keyword_trad
    else:
        print('請求失敗')

