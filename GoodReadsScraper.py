from requests_html import HTMLSession

s = HTMLSession()

url = 'https://www.goodreads.com/list/show/35857.The_Most_Popular_Fantasy_on_Goodreads?page=1'

r = s.get(url)

Books = (r.html.find('#all_votes tr'))

#Domain = "https://www.goodreads.com"
# I will add to join this with the for loop's results
for item in Books:
    print (item.find('a', first=True).attrs['href'])