from functions import get_book_page, get_book_urls, get_book_page_contents, get_category
import csv  

book_info = get_book_page('https://books.toscrape.com/catalogue/lost-among-the-living_31/index.html') 
print(book_info)

"""
with open('book_page_info.csv', 'w', encoding = 'utf-8-sig') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows([book_info])    
"""


for i in range(1,3):
    book_urls = get_book_urls(f'https://books.toscrape.com/catalogue/category/books/mystery_3/page-{i}.html')
    print(book_urls)

get_book_page_contents(book_urls)

category_links = get_category()