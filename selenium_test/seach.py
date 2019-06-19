from selenium import webdriver
driver=webdriver.Firefox()
driver.get("https://baike.baidu.com/item/%E7%A6%8F%E5%B8%83%E6%96%AF%E5%AF%8C%E8%B1%AA%E6%A6%9C/7365918?fr=aladdin")
table=driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[2]/table[1]")
trlist = table.find_elements_by_tag_name("tr")
for tr in trlist:
    tdlist=tr.find_elements_by_tag_name("td")
    for td in tdlist:
        print(td.text,"\t")
    print()

driver.quit()