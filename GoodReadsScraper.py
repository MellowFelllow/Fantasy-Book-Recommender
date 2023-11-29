from requests_html import HTMLSession

s = HTMLSession()

url = 'https://www.goodreads.com/list/show/35857.The_Most_Popular_Fantasy_on_Goodreads?page=1'

r = s.get(url)

print (r.text)

