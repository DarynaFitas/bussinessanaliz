from selenium import webdriver
import csv


driver = webdriver.Chrome()

driver.get("https://www.olx.ua/elektronika/foto-video/fotoapparaty-camery/")

advertisements = driver.find_elements_by_class_name("offer-wrapper")


with open('photo_cameras_olx.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Назва', 'Ціна', 'Місце', 'Дата продажу'])


    for ad in advertisements:
        title = ad.find_element_by_class_name("marginright5").text
        price = ad.find_element_by_class_name("price").text
        location = ad.find_element_by_class_name("breadcrumb").text
        date = ad.find_element_by_class_name("breadcrumb").text.split(",")[-1].strip()
        writer.writerow([title, price, location, date])


driver.quit()