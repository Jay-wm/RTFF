import requests
import lxml.html
import csv
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

'''货币基金筛选'''

def get_found():
    '''将每个基金的源代码放到数组中'''
    Found_body_list = driver.find_elements_by_xpath('//*[@id="dbtable"]/tbody/tr')
    return Found_body_list

def get_foundsinfo(found_body_list):
    '''获取每个基金的信息：基金代号、基金名称、基金详细页面网址、五年收益率'''
    '''获取基金信息，并将其存入数组'''
    for each in found_body_list:
        # Found_url.append(each.xpath('//tbody/tr/td[3]/@href')[0])
        # Found_ticker.append(each.xpath('//tbody/tr/td[3]/a/text()')[0])
        # Found_name.append(each.xpath('//tbody/tr/td[4]/a/text()')[0])
        # Found_rate_return.append(each.xpath('//tbody/tr/td[17]/text()')[0])
        print(each)
        Found_url.append(each.find_elements_by_xpath('//tbody/tr/td[3]/@href')[0])
        Found_ticker.append(each.find_elements_by_xpath('//tbody/tr/td[3]/a/text()')[0])
        Found_name.append(each.find_elements_by_xpath('//tbody/tr/td[4]/a/text()')[0])
        Found_rate_return.append(each.find_elements_by_xpath('//tbody/tr/td[17]/text()')[0])
        print(Found_url)

def get_foundinfo(found_url):
    '''获取每个基金的详细信息：成立时间、费率等'''
    for url in found_url:
        '''初始化基金详细页面'''
        # html_FoundInfo = requests.get(url).content.decode()
        # selector1 = lxml.html.fromstring(html_FoundInfo)
        # Found_date.append(selector1.xpath('//tbody/tr[2]/td[1]/text()')[0])
        print(url)
        Found_date.append(driver.find_elements_by_xpath('//tbody/tr[2]/td[1]/text()')[0])
        print(Found_date)

        '''获得费率'''
        rate_url = selector1.xpath('//*[@id="body"]/div[4]/div[9]/div/div/div[3]/ul/li[14]/a/@href')[0]
        html_rate = requests.get(rate_url).content.decode()
        selector2 = lxml.html.fromstring(html_rate)
        Found_rate_1.append(selector2.xpath('//tbody/tr/td[2]')[0])
        Found_rate_2.append(selector2.xpath('//tbody/tr/td[4]')[0])
        Found_rate_3.append(selector2.xpath('//tbody/tr/td[6]')[0])



'''货币基金近五年收益排行榜网址'''
url = 'http://fund.eastmoney.com/data/hbxfundranking.html#t;c0;r;sSYL_5N;ddesc;pn50;mga;os1;'

driver = webdriver.Chrome('./chromedriver')
driver.get(url)
try:
    WebDriverWait(driver, 60).until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="dbtable"]/tbody/tr[10]/td[2]'), '10'))
except Exception as _:
    print('网页加载太慢了，不等了。')


'''初始化数组'''
Found_body_list = []
Found_url = []
Found_ticker = []
Found_name = []
Found_date = []
Found_rate_return = []
Found_rate_1 = []
Found_rate_2 = []
Found_rate_3 = []
data = []

'''获取基金数组'''
get_found()

'''获取每个基金基本信息'''
get_foundsinfo(Found_body_list)

'''获取基金的成立时间与费率'''
get_foundinfo(Found_url)

'''将每个基金的信息以字典形式组成数组'''
for i in range(len(Found_ticker)):

    dict = {'Found_ticker': Found_ticker[i], 'Found_name': Found_name[i], 'Found_date': Found_date[i],
            'Found_rate_return': Found_rate_return[i], 'Found_rate_1': Found_rate_1[i],
            'Found_rate_2': Found_rate_2[i], 'Found_rate_3': Found_rate_3[i]}
    data.append(dict)

'''将基金信息写入Excel'''
titles = ['Found_ticker', 'Found_name', 'Found_date', 'Found_rate_return', 'Found_rate_1', 'Found_rate_2', 'Found_rate_3']
file_name = '货币基金筛选.csv'
with open(file_name, 'w', newline = '', encoding = 'utf-8') as f:
    writer = csv.DictWriter(f, fieldnames = titles)
    writer.writeheader()
    writer.writerows(data)