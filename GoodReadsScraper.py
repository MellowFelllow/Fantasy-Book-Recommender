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

Test_Link = 'https://www.goodreads.com/book/show/186074.The_Name_of_the_Wind'

r = s.get(Test_Link)

BookName = r.html.find('h1.Text.Text__title1', first=True).text
BookAuthor = r.html.find('span.ContributorLink__name', first=True).text
BookRating = r.html.find('div.RatingStatistics__rating', first=True).text
