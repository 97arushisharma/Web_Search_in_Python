import speech_recognition as sr
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from googlesearch import search
import urllib , webbrowser
<<<<<<< HEAD
from bs4 import BeautifulSoup
=======
>>>>>>> 08a411ce2670840db4db17d5423c5e817ed046d0
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

<<<<<<< HEAD

#for x in filtered_sent:
#	for j in search(x, tld='com', lang='en', num=1, stop=1, pause=2):
#		usock=urllib.request.urlopen(j)
#		webbrowser.open_new(j)
		
output_file=open('news.txt', 'w')
for j in search(a1, tld='com', lang='en', num=1, stop=1, pause=2):
	usock=urllib.request.urlopen(j)
	soup = BeautifulSoup(usock, 'html.parser')
	# Take out the <div> of name and get its value
	i=1
	name_box=" "
	while name_box :
		name_box = soup.find_all('p')[i].get_text()
		print(name_box)
		output_file.write("%s\n" % name_box)
		i=i+1
	#webbrowser.open_new(j)



# specify the url
#quote_page = 'https://www.indiatoday.in/movies/bollywood/story/how-did-sridevi-die-1177180-2018-02-25'

# query the website and return the html to the variable ‘page’
#page = urllib.request.urlopen(quote_page)

# parse the html using beautiful soup and store in variable `soup`


=======
# => via regular expression

for x in filtered_sent:
	for j in search(x, tld='com', lang='en', num=1, stop=1, pause=2):
		usock=urllib.request.urlopen(j)
		webbrowser.open(j)
		
>>>>>>> 08a411ce2670840db4db17d5423c5e817ed046d0

#print(page.find(x.encode()))

#filtered_sent= [w for w in words if not w in stop_words]
 
#try:
#    print("You said " + a1)
#except sr.UnknownValueError:
#    print("Could not understand audio")
#except sr.RequestError as e:
#    print("Could not request results; {0}".format(e))
 
