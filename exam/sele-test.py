from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
#用于获取命令行参数
import sys  
#用于提取年月日
from datetime import datetime  
#导入货币库
from currencyinfo import serial_currencies

date_str=str()
currency=str()
year=int()
month=int()
day=int()




def crawl():
    #指定驱动浏览器
    driver=webdriver.Chrome()
    driver.maximize_window()
    url='https://www.boc.cn/sourcedb/whpj/'

    driver.get(url)
    try:
        #选年
        enter_date1=driver.find_element(by=By.XPATH,value='//*[@id="erectDate"]')
        enter_date1.click()
        sleep(1)
        find_year=driver.find_element(by=By.XPATH,value='//*[@id="calendarYear"]')
        find_year.click()
        sleep(1)
        cha=year-2000
        path='//*[@id="calendarYear"]/option['+str(cha)+']'
        choose_year=driver.find_element(by=By.XPATH,value=path)
        choose_year.click()
        sleep(1)
    except :
        print("无法选择年\n")
    #选月
    find_month=driver.find_element(by=By.XPATH,value='//*[@id="calendarMonth"]')
    find_month.click()
    sleep(1)
    path='//*[@id="calendarMonth"]/option['+str(month)+']'
    choose_month=driver.find_element(by=By.XPATH,value=path)
    choose_month.click()
    sleep(1)

    #选日
    rows=driver.find_elements(by=By.XPATH,value='//tr[@align="center"]')
    for row in rows:
        days=row.find_elements(by=By.XPATH,value='./td')
        for one_day in days:
            if one_day.text==str(day):
                one_day.click()
                sleep(1)
                break

    try:
        #选年
        enter_date2=driver.find_element(by=By.XPATH,value='//*[@id="nothing"]')
        enter_date2.click()
        sleep(1)
        find_year=driver.find_element(by=By.XPATH,value='//*[@id="calendarYear"]')
        find_year.click()
        sleep(1)
        cha=year-2000
        path='//*[@id="calendarYear"]/option['+str(cha)+']'
        choose_year=driver.find_element(by=By.XPATH,value=path)
        choose_year.click()
        sleep(1)
    except:
        print("选年出错\n")
    #选月
    find_month=driver.find_element(by=By.XPATH,value='//*[@id="calendarMonth"]')
    find_month.click()
    sleep(1)
    path='//*[@id="calendarMonth"]/option['+str(month)+']'
    choose_month=driver.find_element(by=By.XPATH,value=path)
    choose_month.click()
    sleep(1)
    #选日
    rows=driver.find_elements(by=By.XPATH,value='//tr[@align="center"]')
    for row in rows:
        days=row.find_elements(by=By.XPATH,value='./td')
        for one_day in days:
            if one_day.text==str(day):
                one_day.click()
                sleep(1)
                break

    find_currency=driver.find_element(by=By.XPATH,value='//*[@id="pjname"]')
    find_currency.click()

    path='//*[@id="pjname"]/option['+str(serial_currencies[currency])+']'
    choose_currency=driver.find_element(by=By.XPATH,value=path)
    choose_currency.click()
    sleep(1)

    #查找
    search=driver.find_element(by=By.XPATH,value='//*[@id="historysearchform"]/div/table/tbody/tr/td[7]/input')
    search.click()
    sleep(1)
    #已进入详情页
    #找到第一行的现汇卖出价数据并输出
    price=driver.find_element(by=By.XPATH,value='//tr[@class="odd"]/td[4]').text
    print("现汇卖出价:",price)



  
def main():  
    global date_str,currency,year,month,day
    # 获取命令行参数  
    date_str = sys.argv[1]  
    currency = sys.argv[2]  
    #提取年月日
    date_obj=datetime.strptime(date_str, '%Y%m%d')
    year=date_obj.year
    month = date_obj.month  
    day = date_obj.day 
    # print(year, month, day)
    crawl()
  
if __name__ == "__main__":  
    main()