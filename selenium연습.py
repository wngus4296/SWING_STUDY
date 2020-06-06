from selenium import webdriver

driver = webdriver.Chrome(r"C:\Users\SAMSUNG\Desktop\chromedriver_win32\chromedriver")
driver.get(r"http://zzzscore.com/1to50/?ts=1591020560516")

numbtn = driver.find_elements_by_xpath(r'//*[@id="grid"]/div[*]')

for i in range(1, 51):
    for n in numbtn:
        if n.text == str(i):
            n.click()
            print(str(i) + " click!")
            break
