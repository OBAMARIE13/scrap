import requests
from bs4 import BeautifulSoup





# url = "https://ci.opera.news/"
# response = requests.get(url)
# if response.ok:

#     soup = BeautifulSoup(response.text, "html.parser")
#     categorie_container = soup.find('div', {'class': 'category-container'})
#     categorie_items = categorie_container.findAll('a', {'class': 'sidenav-item'})
#     locals_db = []
#     for cat_item in categorie_items:
#         cat_dict = {}
#             # Verifie si categorie existe

#         # url: href
#         cat_dict['categorie_liens'] = "https://ci.opera.news/" + cat_item['href']
#         cat_dict['categorie_nom'] = cat_item.text
#         locals_db.append(cat_dict)
#     print(locals_db)

def scrap():
    locals_db = []
    url = "https://ci.opera.news/ci/fr/latest"
    
    response = requests.get(url)

    def sections_detail(url):
            # ________get_detail______________
    
        detail = ""
        response = requests.get(url)
        if response.ok:
            soup = BeautifulSoup(response.text, 'html.parser')
            detail = soup.find('div', {'class': 'article-card category-list-default'})
        return detail
        print(detail)

    url = "https://ci.opera.news/ci/fr/latest"
    
    if response.ok:
        soup = BeautifulSoup(response.text, "html.parser")
        other_article = list(soup.findAll('div', {'class': 'article-card category-list-default'}))
        dicts = {}
        
        for item in other_article:
            title = item.find('p', {'class': 'title'})
            lien_title = title.find('a')
            picture = item.find('img')

            dicts['title'] = title.text
            dicts['lien_title'] = lien_title['href']
            dicts['picture'] =  picture['src']
            dicts['detail'] = sections_detail(dicts['lien_title'])
            locals_db.append(dicts)
        print(locals_db)
    
    return locals_db


        
    # ________________________


if __name__ == '__main__':
    scrap()
    


    

    