import requests
from bs4 import BeautifulSoup


url = "https://ci.opera.news/ci/fr/latest"


response = requests.get(url)
if response.ok:
    soup = BeautifulSoup(response.text, 'html.parser')
    titre = soup.find('h1')
    print(titre.text)


if response.ok:
    soupe = BeautifulSoup(response.text, 'html.parser')
    bloc = soupe.find('div', {'class': 'article-card category-list-primary'})
    lien = bloc.find('a')
    image = bloc.find[('img', {'class': 'cover'})]

    # for i in bloc:
    #     dictionnaire = {}


        # lien = i.find('a', {'class': 'cover'})
        # image = i.find('img', {'class': 'cover'})
        # titre_image = i.find('p', {'class': 'tax-name'})
        # titre_bloc = i.find('p', {'class': 'title'})


    # dictionnaire['lien'] = lien['href']
    # dictionnaire['src_image'] = image['src']
    # dictionnaire['titre_image'] = titre_image.text
    # dictionnaire['titre_bloc'] = titre_bloc.text

    # liste.append(i.dictionnaire)

    print(image)









    url = "https://ci.opera.news/ci/fr/sports"

    
    dictionnaire = {}

    response = requests.get(url)
    if response.ok:
        soupe = BeautifulSoup(response.text, 'html.parser')

        parent = soupe.find('div', {'class': 'category-list-body'})
    
        
#             # ________________premiere partie_______________
        
        bloc = parent.find('div', {'class': 'article-card category-list-primary'})

        lien_image = bloc.find('a')
        bloc_image = bloc.find('a', {'class': 'cover'})
        image = bloc_image.find('img')

        titre_article = bloc.find('p', {'class': 'title'})

        categories = bloc.find('p', {'class': 'tax-name'})


        heure_bloc = bloc.find('p', {'class': 'extra'})
        heure = heure_bloc.find('span')
        icones = heure_bloc.find('img')
        likes_nombre = heure_bloc.find('span', {'class': 'comment-num'})


        dictionnaire['lien_image'] =  lien_image['href']
        dictionnaire['src_image'] =  "https://ci.opera.news/i" +  image['src']
        dictionnaire['titre_article'] = titre_article.text 
        dictionnaire['categories'] = categories.text
        dictionnaire['heure'] = heure.text
        dictionnaire['src_icones'] = "https://ci.opera.news/i" + icones['src']
        dictionnaire['likes_nombre'] = likes_nombre.text

        

        # liste.append(dictionnaire)


# # ____________________2 partie(sections)_________________


   

    
    sections = parent.find('section', {'class': 'category-second-group'})
    div_bloc = list(sections.findAll('div', {'class': 'article-card category-card'}))
    
    for items in div_bloc:
        dictionnaire__ = {}
        
        lien = items.find('a')
        images = items.find('img')
        categorie = items.find('p', {'class': 'tax-name'})
        lien_categorie = categorie.find('a')

        titre_image = items.find('p', {'class': 'title'})
        lien_titre = titre_image.find('a')

        footer = items.find('footer', {'class': 'extra'})
        temps = footer.find('span')
        icone = footer.find('img')
        like = footer.find('span', {'class': 'comment-num'})
        


        dictionnaire__['lien'] =  lien['href']
        dictionnaire__['src_image'] =  "https://ci.opera.news/i" +  images['src']
        dictionnaire__['categorie'] = lien_categorie.text
        dictionnaire__['lien_categorie'] = lien_categorie['href']
        dictionnaire__['titre_image'] = titre_image.text
        dictionnaire__['temps'] = temps.text
        dictionnaire__['src_icone'] = "https://ci.opera.news/i" + icone['src']
        dictionnaire__['like'] = like.text
        dictionnaire__['detail'] = sections_detail(lien['href'])

        # liste.append(dictionnaire__)
        print(dictionnaire__['detail'])



# ______________3e partie________________

    


