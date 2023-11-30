from requests_html import HTMLSession

s = HTMLSession()

def get_book_links(page):
    url = f'https://www.goodreads.com/list/show/35857.The_Most_Popular_Fantasy_on_Goodreads?page={page}'
    links = []
    r = s.get(url)
    Books = (r.html.find('#all_votes tr'))
    Domain = "https://www.goodreads.com"

    for item in Books:
        links.append(Domain+(item.find('a', first=True).attrs['href']))
    return links 

