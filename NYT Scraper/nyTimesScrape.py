import csv
from nytimesarticle import articleAPI
import time

api = articleAPI('ec4da91764da4217983fadb8c85f1dca')

articles = api.search(q = "Trump",
		fq = {'headline':'Trump'},
		begin_date = '20160707',
		end_date = '20161107',
		fl = 'headline,pub_date,word_count',
		sort='oldest',
		page = '101')


print articles

print "----------------------------------------"


all_articles = []
for j in range(0,100): #NYT limits pager to first 100 pages. But rarely will you find over 100 pages of results anyway.
	time.sleep(6) #API calls limited to 5 seconds. make it 6 so it doesn't get angry
	articles = api.search(q = "Trump",
		fq = {'headline':'Trump'},
		begin_date = '20160707',
		end_date = '20161107',
		fl = 'headline,pub_date,word_count',
		sort='oldest',
		page = str(j))

	print j
	news = []
	
	for i in articles['response']['docs']:
		dic = {}
		dic['headline'] = i['headline']['main'].encode("utf8")
		dic['date'] = i['pub_date'][0:10] # cutting time of day.
		dic['word_count'] = i['word_count']
		news.append(dic)


	articles = news
	print articles
	print "---------------------------------------"
	all_articles = all_articles + articles


print articles
# q: 	Trump
# fq:	headline:'Trump'
# begin_date:	20160707
# end_date:		20161107
# fl:			headline,pub_date,word_count
# page: mother fucker all of them 