
#create project
scrapy startproject spider01_dmoz

#run spider
scrapy crawl dmoz

#run spider and output items.json
scrapy crawl dmoz -o items.json -t json


#debug
scrapy shell http://www.dmoz.org/Computers/Programming/Languages/Python/Books/




