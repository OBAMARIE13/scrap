import requests
from bs4 import BeautifulSoup


# _________scrap opera_news____________
def scrap_main():
    url = "https://ci.opera.news/"
    
    locals_db = []
    # ___________get catgorie________
    def get_category():
        url = "https://ci.opera.news/"
        response = requests.get(url)
        if response.ok:
            soup = BeautifulSoup(response.text, "html.parser")
            categorie_container = soup.find('div', {'class': 'category-container'})
            categorie_items = categorie_container.findAll('a', {'class': 'sidenav-item'})
            cat_dict = {}
            for cat_item in categorie_items:
                # Verifie si categorie existe
        
                # url: href
                cat_dict['categorie_liens'] = cat_item['href']
                cat_dict['categorie_nom'] = cat_item.text
                
            
            locals_db.append(cat_dict)

            



    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.text, "html.parser")
        parent = soup.find('div', {'class': 'category-list-body'})

    # def scrap_categorie_article(categorie_liens, categorie_nom):
    #     other_article = list(parent.findAll('div', {'class': 'article-card category-list-default'}))
    #     for items in other_article:
    #         dicts = {}

    #         title = items.find('p', {'class': 'title'})
    #         lien_title = title.find('a')
    #         picture = items.find('img')

    #         dicts['title'] = title.text
    #         dicts['lien_title'] = lien_title['href']
    #         dicts['picture'] = "https://ci.opera.news/i" + picture['src']
    #         dicts['detail'] = sections_detail(lien_title['href'])

    #     locals_db.append(dicts)

            

    # def sections_detail(getLink):
    #     # ________get_detail______________
    #     detail = ""
    #     response = requests.get(url)
    #     if response.ok:
    #         soup_detail = BeautifulSoup(response.text, 'html')
    #         detail = soup_detail.find('div', {'class': 'article-card category-list-default'})
    #     return detail
    
    # # ________________________




    #return(locals_db)


get_category()