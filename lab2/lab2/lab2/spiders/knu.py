import scrapy
from bs4 import BeautifulSoup
from lab2.items import FacultyItem


class UzhnuSpider(scrapy.Spider):

    name = "knu"
    allowed_domains = ["knu.ua"]

    start_urls = ["https://knu.ua/ua/departments"]

    def parse(self, response):
        soup = BeautifulSoup(response.body,  "html.parser")

        fac_list = soup.find(class_="departments_unfolded")
        for li in fac_list.find_all("li"):
            a = li.find("a")

            fac_name = a.find(string=True, recursive=False)
            fac_url = f"https://knu.ua{a.get('href')}"

            yield FacultyItem(
                name=fac_name,
                url=fac_url
            )

 