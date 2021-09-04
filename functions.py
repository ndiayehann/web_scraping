import requests
from bs4 import BeautifulSoup as bs

def get_book_page(book_url):
    
    # Connexion à la page produit choisie
    url = book_url
    response = requests.get(url)

    # On parse le contenu HTML obtenu
    soup = bs(response.content, 'html.parser')
    # Extraction des éléments de la table contenant les headers
    table = soup.find('table', class_= 'table table-striped')
    #print(table)
    upc = table.find('tr').td.text.strip('\n')  
    product_type = table.find('tr').find_next_siblings()[0].get_text().strip('\n')
    price_excluding_tax = table.find('tr').find_next_siblings()[2].td.text
    price_including_tax = table.find('tr').find_next_siblings()[3].td.text
    number_available = table.find('tr').find_next_siblings()[4].td.text
    review_rating = table.find('tr').find_next_siblings()[5].td.text
    category = soup.find('ul', class_='breadcrumb').li.find_next_siblings()[1].text.replace('\n', '')
    print(category)
    # Ajout de la colonne description
    product_description = soup.find('div', class_='sub-header').find_next_siblings()[0].text.strip('\n')

    # Ajout de la colonne title
    title = soup.find('div', class_='col-sm-6 product_main').h1.text.strip('\n')

    # Ajout de la colonne image_url
    image = soup.find('div', class_='item active')
    base_image_url = 'https://books.toscrape.com/'
    for image in image.find_all('img'):
        image_url = base_image_url + image['src'].strip('../../') 

    # Récupération de l'URL de la page produit choisie
   # product_page_url = soup.find('ul', class_='breadcrumb').find_all('a')[2]['href']
    base_url = 'books.toscrape.com/catalogue/' 
    partial_link= soup.find('div', class_='image_container').find('a')['href'].strip('../')
    product_page_url = base_url + partial_link
    data = [{
        'product_page_url': product_page_url,
        'upc' : upc,
        'title' : title,
        'price_including_tax' : price_including_tax,
        'price_excluding_tax' : price_excluding_tax,
        'number_available' : number_available,
        'product_description' : product_description,
        'product_type' : product_type,
        'review_rating' : review_rating,
        'image_url' :  image_url,
        'category' : category
         }]
    
    return data

    # Récupération des urls des livres en fonction de la catégorie 
def get_book_urls(book_link):
    url = book_link
    r = requests.get(url)
    elt = bs(r.content, 'html.parser')

    url_tags = elt.find('ol', class_='row').find_all('div', class_='image_container')
    base_url = 'https://books.toscrape.com/catalogue/'
    book_urls = []

    for item in url_tags:
        for link in item.find_all('a'):
            book_urls.append(base_url + link['href'].strip('../../../'))
    #print(book_urls)
    return book_urls

    # Récupération des infos des livres en fonction de la catégorie 
def get_book_page_contents(book_urls):
    
    for i in range(len(book_urls)):
        info = get_book_page(book_urls[i])
        print (info)
    return info

    # Définition d'une fonction pour charger toutes les urls des différentes catégories
def get_category():
    
    url = 'https://books.toscrape.com/catalogue/page-1.html'
    response = requests.get(url)
    soup = bs(response.content, 'html.parser')
    #print(soup.prettify())
    parent_category_tags = soup.find('ul', class_= 'nav nav-list').li
    children_category_tags = parent_category_tags.findChildren('ul', recursive=False)
    #print(children_category_tags)

    category_links = []

    for item in children_category_tags:
        for link in item.find_all('a'):
            category_links.append(url.replace('page-1.html', '') + link['href'])
    print(category_links)
    return category_links

def all_books_info(category_links):
    for i in range(len(category_links)):
        all_info = get_book_page_contents(get_book_urls(category_links[i]))
        return all_info

