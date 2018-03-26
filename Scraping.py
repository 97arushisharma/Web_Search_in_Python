import urllib.request
from bs4 import BeautifulSoup

# specify the url
quote_page = 'https://www.indiatoday.in/movies/bollywood/story/how-did-sridevi-die-1177180-2018-02-25'

# query the website and return the html to the variable ‘page’
page = urllib.request.urlopen(quote_page)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')

# Take out the <div> of name and get its value
#name_box = soup.find('p', attrs={'class' : 'description tbl-forkorts-article'})
#name_box = soup.find("div", class_="description tbl-forkorts-article")
output_file=open('news.txt', 'w')
i=1
name_box=" "
while name_box :
	name_box = soup.find_all('p')[i].get_text()
	print(name_box)
	output_file.write("%s\n" % name_box)
	i=i+1


#name = name_box.text # strip() is used to remove starting and trailing



