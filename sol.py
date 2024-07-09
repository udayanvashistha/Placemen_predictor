from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get(r" https://www.dailymotion.com/tseries2")
driver.implicitly_wait(5)
hrefs = [video.get_attribute('href') for video in driver.find_elements(By.TAG_NAME,'a')]
freq = {}
a = "https://www.dailymotion.com/video/"
ans = '0'
freq[ans]=0
for i in range(min(len(hrefs),500)):
    x = hrefs[i]
    if(x[:34]!=a):
        continue
    for ch in x[34:]:
        if(ch not in freq):
            freq[ch]=1
        else:
            freq[ch]+=1
        if(freq[ch]>freq[ans]):
            ans = ch
print(ans+":"+str(freq[ans]))