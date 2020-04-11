from selenium import webdriver
from time import sleep
import urllib.request
import os


def movies(Name):
    driver = webdriver.Chrome(r'C:\Users\Sri\Downloads\chromedriver')
    driver.maximize_window()
    driver.get('https://www.allmovie.com/')
    sleep(2)
    search = driver.find_element_by_xpath(
        '/html/body/div[2]/div[1]/div/div/div[2]/form/input[2]')
    search.send_keys(Name)  # remove '/' from movie
    btn_search = driver.find_element_by_xpath(
        '/html/body/div[2]/div[1]/div/div/div[2]/form/input[1]')  # find by xpath
    btn_search.click()
    sleep(5)

    click_link = driver.find_element_by_xpath(
        '//*[@id="cmn_wrap"]/div[1]/div[2]/div[1]/ul/li[1]/div[2]/div[1]/a')  # explicit wait time once the element is found if will break loop
    click_link.click()
    sleep(5)

    driver.execute_script('window.scrollTo(0,200)')
    img = driver.find_element_by_class_name(
        "poster-launch").get_attribute('src')
    print(img)

    if not os.path.exists('img'):
        os.makedirs('img')
    urllib.request.urlretrieve(img, 'img/{0}.jpg'.format(Name))
    driver.close()


links = open('movies_name_test.txt', 'r')
lst = links.read()
links.close()

movie_txt = lst.split('\n')
for i in movie_txt:  # each movie_name
    movies(i[:-1])
