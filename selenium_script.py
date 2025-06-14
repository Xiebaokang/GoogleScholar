import os
import time, random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from script import readText, getCitePageUrl, CiteNextUrl, saveData


def createBrowser():
  dirname = os.getcwd()
  os.environ['Path'] += dirname
  chromedriver_path = Service(os.path.join(dirname, "chromedriver.exe"))
  browser = webdriver.Chrome(service=chromedriver_path)
  return browser

def parsePage(browser):
  # parse Page
  pdfs, words = [], []
  mid = browser.find_element(By.ID, "gs_res_ccl_mid")
  items = mid.find_elements(By.CLASS_NAME, "gs_scl")
  for item in items:
    cid = item.get_attribute("data-cid")
    title = item.find_element(By.ID, cid)
    pdfs.append([title.text, title.get_attribute("href")])
    item.find_element(By.CLASS_NAME, "gs_nph").click()
    time.sleep(random.randint(2, 3))
    citt = browser.find_element(By.ID, "gs_citd")
    text = citt.find_element(By.ID, "gs_citt").find_element(By.CLASS_NAME, "gs_citr").text
    words.append(text)
    browser.find_element(By.ID, "gs_cit-x").click()
    time.sleep(random.randint(1, 2))
  return words, pdfs
    
  
def run(browser):
  browser.maximize_window()
  for name in readText("./src_paper.txt"):
    print(f"Getting cite: {name}")
    all_words, all_pdfs = [], []
    citeUrl = getCitePageUrl(name)
    browser.get(citeUrl)
    # print(browser.page_source)
    # print(CiteNextUrl(browser.page_source))
    while True:
      words, pdfs = parsePage(browser)
      all_words += words
      all_pdfs += pdfs
      next_url = CiteNextUrl(browser.page_source)
      if next_url is None:
        break
      browser.get(next_url)
      time.sleep(random.randint(5, 8))
    saveData(all_words, all_pdfs, name)
    print("== Finished.")

if __name__ == "__main__":
  browser = createBrowser()
  run(browser)