import requests
from bs4 import BeautifulSoup


# url = "https://ci.opera.news/ci/fr/latest"
# url = "https://ci.opera.news/ci/fr/sports"


#  connaitre si le site peut etre scrapper
# ------------------------------



# -----------------------
# tt les titres
        # response = requests.get(url)
        # print(response.headers)
# --------------------

# le code source html
# -------------------------------
        # response = requests.get(url)
        # if response.ok:
        #     soup = BeautifulSoup(response.text)
        #     print(soup)
# -------------------------------

# un seul titre autre methode
# ------------------------
        # response = requests.get(url)
        # if response.ok:
        #     soup = BeautifulSoup(response.text, 'html')
        #     title = soup.find('title')
        #     print(title)
# ------------------------


# tt les titres autre methode
# ------------------------
# response = requests.get(url)
# if response.ok:
#     soup = BeautifulSoup(response.text)
#     tds = soup.findAll('td')
#     [print(str(td)+ '\n\n') for td in tds]
# ------------------------
