from functions import get_book_page
import csv  

book_info = get_book_page('https://books.toscrape.com/catalogue/lost-among-the-living_31/index.html') 
print(book_info)

with open('book_page_info.csv', 'w', encoding = 'utf-8-sig') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows([book_info])    
