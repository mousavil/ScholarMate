import time
import config as config
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=selenium-user-data")
options.add_argument("--disable-extensions")
options.add_argument("start-maximized")
timeout = 30
driver = webdriver.Chrome("../chromedriver", options=options)
driver.implicitly_wait(timeout)


def wait_for_element(locator):
    return WebDriverWait(driver, 30).until(
        EC.presence_of_element_located(locator)
    )


def sign_in(url: str,
            email: str,
            password: str) -> None:
    driver.get(url)

    time.sleep(10)

    try:
        wait_for_element((By.NAME, 'identifier')).send_keys(email)


        wait_for_element((By.NAME, 'password')).send_keys(password)

    except:
        return

    continue_button = wait_for_element((By.XPATH, '//*[@id="__next"]/div/div/div/div/div[3]/form/button[2]'))

    continue_button.click()

    time.sleep(10)


def redirect_to_templates(url: str) -> None:
    driver.get(url)


def select_essay() -> None:
    essay_button = wait_for_element((By.XPATH, '//*[@id="modal-root"]/div[1]/div/div/div[2]/div/div/div[2]/div/button[1]'))

    essay_button.click()

    time.sleep(10)


def fill_details(title: str,
                                        description: str,
                                        keywords: list) -> None:

    title_box = wait_for_element((By.XPATH, '//*[@id="modal-root"]/div[1]/div/div/div[1]/div[2]/div/h1'))
    title_box.send_keys(title)

    description_box = wait_for_element((By.XPATH, '//*[@id="modal-root"]/div[1]/div/div/div[1]/div[3]/div'))
    description_box.send_keys(description)

    keywords_box = wait_for_element((By.XPATH, '//*[@id="modal-root"]/div[1]/div/div/div[1]/div[4]/div/ul/li/p'))
    keywords_box.send_keys(', '.join(keywords))

    scroll_down()

    time.sleep(10)

    generate_essay_button = wait_for_element((By.XPATH, '//*[@id="modal-root"]/div[1]/div/div/button'))
    generate_essay_button.click()

    time.sleep(15)


def fill_outline() -> None:
    scroll_down()

    time.sleep(10)

    create_point_button = wait_for_element((By.XPATH, '//*[@id="modal-root"]/div[1]/div/div/button'))
    create_point_button.click()                        

    time.sleep(15)


def fill_points() -> None:
    scroll_down()

    time.sleep(10)

    finish_button = wait_for_element((By.XPATH, '//*[@id="modal-root"]/div[1]/div/div/div[2]/button[2]'))
    finish_button.click()                       

    time.sleep(15)


def fill_editor():
    scroll_down()

    time.sleep(15)

    soup = BeautifulSoup(driver.page_source, "html.parser")

    output=''
    for tag in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p']):        
        output = output + tag.text + ' \n'

    with open('output.txt', 'w') as f:
        f.write(output)

    time.sleep(10)


def scroll_down():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")