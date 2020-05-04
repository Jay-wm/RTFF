import lxml.html
import csv
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

'''货币基金筛选'''
def get_found():
    '''货币基金近五年收益排行榜网址'''
    url = 'http://fund.eastmoney.com/data/hbxfundranking.html#t;c0;r;sSYL_5N;ddesc;pn50;mga;os1;'

    '''初始化数组'''
    Found_url = []
    Found_ticker = []
    Found_name = []
    Found_return_date = []
    Found_return = []
    Found_rate_return = []
    data = []

    '''初始化driver'''
    driver = webdriver.Chrome('./chromedriver')
    driver.get(url)
    try:
        WebDriverWait(driver, 60).until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="dbtable"]/tbody/tr[10]/td[2]'), '10'))
    except Exception as _:
        print('网页加载太慢了，不等了。')

    '''获得排行榜的每个基金的源代码'''
    Found_page_source = driver.page_source
    selector_1 = lxml.html.fromstring(Found_page_source)
    Found_body_list = selector_1.xpath('//*[@id="dbtable"]/tbody/tr')

    for each in Found_body_list:
        Found_url.append(each.xpath('td[3]/a/@href')[0])
        Found_ticker.append(each.xpath('td[3]/a/text()')[0])
        Found_name.append(each.xpath('td[4]/a/text()')[0])
        Found_return_date.append(each.xpath('td[5]/text()')[0])
        Found_return.append(each.xpath('td[6]/text()')[0])
        Found_rate_return.append(each.xpath('td[17]/text()')[0])

    for i in range(len(Found_name)):
        dict = {'基金代码': Found_ticker[i], '基金名称': Found_name[i], '日期': Found_return_date[i],
                '万份收益': Found_return[i], '近5年回报率': Found_rate_return[i]}
        data.append(dict)

    '''将基金信息写入Excel'''
    titles = ['基金代码', '基金名称', '日期', '万份收益', '近5年回报率']
    file_name = '货币基金筛选.csv'
    with open(file_name, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=titles)
        writer.writeheader()
        writer.writerows(data)


get_found()
