# SeleniumTest
Selenium 爬虫笔试代码 已完结

sele-test.py 是主程序 currencyinfo.py包含货币信息。实现功能：
输入：日期、货币代号
输出：该日期该货币的“现汇卖出价”

运行方式：进入test目录，打开终端输入 py sele-test.py 日期 货币

示例：py sele-test.py 2022102 USD
输出：现汇卖出价: 713.67

提示：因为是小规模程序，为了debug方便和数据加载，在每次点击一个按钮后都使用了sleep（1），也可以去掉但是为了防止元素还未加载完就开始查找二找不到报错需要等到元素加载。如：

from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC  
try:  
    element = WebDriverWait(driver, 10).until(  
        EC.presence_of_element_located((By.XPATH, '//*[@id="erectDate"]'))  
    )  
finally:  
    driver.quit()
