import speech_recognition as sr
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from googlesearch import search
import urllib , webbrowser
#import re 
 
# get audio from the microphone                                                                       
r = sr.Recognizer()                                                                                   
with sr.Microphone() as source:                                                                       
    print("Speak:")                                                                                   
    audio = r.listen(source) 
a1=r.recognize_google(audio); 

stop_words=set(stopwords.words("english"))
words= word_tokenize(a1);

print(stop_words)

filtered_sent=[]

for w in words:
	if w not in stop_words:
		filtered_sent.append(w)

print(filtered_sent)

 
#page = urllib.request.urlopen("http://google.com").read()

# => via regular expression

for x in filtered_sent:
	for j in search(x, tld='com', lang='en', num=1, stop=1, pause=2):
		usock=urllib.request.urlopen(j)
		webbrowser.open(j)
		

#print(page.find(x.encode()))

#filtered_sent= [w for w in words if not w in stop_words]
 
#try:
#    print("You said " + a1)
#except sr.UnknownValueError:
#    print("Could not understand audio")
#except sr.RequestError as e:
#    print("Could not request results; {0}".format(e))
 
