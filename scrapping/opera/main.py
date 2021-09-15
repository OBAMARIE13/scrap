import requests
from bs4 import BeautifulSoup


# _________scrap opera_news____________
# def scrap_main():
# url = "https://ci.opera.news/"

locals_db = []
        # ___________scrap_catgorie________
def get_category():
    url = "https://ci.opera.news/"
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.text, "html.parser")
        categorie_container = soup.find('div', {'class': 'category-container'})
        categorie_items = categorie_container.findAll('a', {'class': 'sidenav-item'})
        for cat_item in categorie_items:
            cat_dict = {}
                # Verifie si categorie existe
    
            # url: href
            cat_dict['categorie_liens'] = "https://ci.opera.news/" + cat_item['href']
            cat_dict['categorie_nom'] = cat_item.text
            locals_db.append(cat_dict)
        print(locals_db)
        
        
        
    url = "https://ci.opera.news/ci/fr/latest"
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.text, "html.parser")
        parent = soup.find('div', {'class': 'category-list-body'})

    # scrapper les articles des differentes categories

    def scrap_categorie_article(categorie_liens, categorie_nom):
        if response.ok:
            soup = BeautifulSoup(response.text, "html.parser")
            other_article = list(soup.findAll('div', {'class': 'article-card category-list-default'}))
            dicts = {}

            for i in other_article:
                title = i.find('p', {'class': 'title'})
                lien_title = title.find('a')
                picture = i.find('img')

                dicts['title'] = title.text
                dicts['lien_title'] = lien_title['href']
                dicts['picture'] = "https://ci.opera.news/" + picture['src']
                # dicts['detail'] = sections_detail(lien_title['href'])
                #locals_db.append(dicts)
            
            
                print(dicts)
                    

    # def sections_detail(getLink):
    #     # ________get_detail______________
    #     detail = ""
    #     response = requests.get(url)
    #     if response.ok:
    #         soup_detail = BeautifulSoup(response.text, 'html')
    #         detail = soup_detail.find('div', {'class': 'article-card category-list-default'})
    #     return detail
    
    # # ________________________



    return locals_db


# get_category()
if __name__ == '__main__':
    get_category()