from requests import get
from bs4 import BeautifulSoup

BASE_URL = "https://knu.ua/ua"
URL = f"{BASE_URL}/departments"

page = get(URL)
soup = BeautifulSoup(page.content, "html.parser")

fac_list = soup.find(class_="b-references__holder")

for li in fac_list.find_all("li"):

    a = li.find("a")

    fac_name = a.find(text=True, recursive=False)

    fac_link = BASE_URL + a.get("href")

    print(f"Назва факультету: {fac_name}")
    print(f"URL: {fac_link}")

    fac_page = get(fac_link)
 
    soup = BeautifulSoup(fac_page.content, "html.parser")
    dep_list = soup.find(class_="b-body__text")

    if dep_list:
        for dep in dep_list.find_all(li, class_="b-body__text"):
            dep_name = dep.text.strip()
            print(f"Назва кафедри: {dep_name}")
    else:
        print("Список кафедр не знайдено")