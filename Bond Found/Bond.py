import datetime
import lxml.html
import csv
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

'''债券基金筛选'''

# 将基金排行榜里面自定义时间在2015/6/1-2016/2/29之间的大盘下跌的这段时间进行排序，得到该页面的源代码
def get_page_sources(url, condition):
    '''初始化driver'''
    driver = webdriver.Chrome('./chromedriver')
    driver.get(url)
    try:
        WebDriverWait(driver, 90).until(EC.present_in_element((By.ID, condition)))
    except Exception as _:
        print('网页加载太慢了，不等了。')

    '''得到排行榜页面源代码并返回'''
    page_source = driver.page_source
    return page_source

# 获取排行榜第num个基金页面的网址
def get_url(foundList_page_source, num):
    address = '//*[@id="fund_list"]/tbody/tr[' + str(num+1) + ']/td[2]/a/@href'
    selector = lxml.html.fromstring(foundList_page_source)
    found_url = selector.xpath(address)[0]
    return found_url

def filter_found(found_url):
    found_page_source = get_page_sources(found_url, '//*[@class="wrapper_min"]')
    selector = lxml.html.fromstring(found_page_source)
    found_name = selector.xpath('//*[@id="body"]/div[12]/div/div/div[1]/div[1]/div/text()')[0]
    found_ticker = selector.xpath('//*[@id="body"]/div[12]/div/div/div[1]/div[1]/div/span[2]/text()')[0]

    '''通过成立日期进行第一次筛选'''
    found_date_establishment0 = selector.xpath('//*[@id="body"]/div[12]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[1]/text()')[0]
    found_date_establishment = found_date_establishment0.replace('：', '')
    zero = datetime.datetime.fromtimestamp(0)

    try:
        d1 = datetime.datetime.strptime(found_date_establishment, fmt)
    except:
        d1 = zero

    try:
        d2 = datetime.datetime.strptime(str(2013-01-01), fmt)
    except:
        d2 = zero

    if d1 >

    found_date_establishment

    return found_name, found_ticker

'''债券基金排行榜网址'''
url = 'http://fund.eastmoney.com/daogou/#dt0;ftzq;rs;sd2015-06-01;ed2016-02-29;pr;cp;rt;tp;rk;se;nx71;scdiy;stdesc;pi1;pn20;zfdiy;shlist'

'''获得债券基金排行榜页面源代码'''
foundList_page_source = get_page_sources(url, '//*[@id="fund_list"]')

'''筛选出5个满足：基金规模-尽量选择规模大的，最好在5-50亿之间，规模太小容易有波动；成立年限-7年以上的债券基金'''
for num in range(1):
    Found_url = get_url(FoundList_page_source, num)
    filter_found(Found_url)





# get_url(Found_page_source, 2)

    # for each in Found_body_list:
    #     Found_url.append(each.xpath('td[3]/a/@href')[0])
    #     Found_ticker.append(each.xpath('td[3]/a/text()')[0])
    #     Found_name.append(each.xpath('td[4]/a/text()')[0])
    #     Found_return_date.append(each.xpath('td[5]/text()')[0])
    #     Found_return.append(each.xpath('td[6]/text()')[0])
    #     Found_rate_return.append(each.xpath('td[17]/text()')[0])

# def get_more_info(Found_url):
#     for
#
#
# def save_data(Found_ticker, Found_name, ):
#     for i in range(len(Found_name)):
#         dict = {'基金代码': Found_ticker[i], '基金名称': Found_name[i], '日期': Found_return_date[i],
#                 '万份收益': Found_return[i], '近5年回报率': Found_rate_return[i]}
#         data.append(dict)
#
#     '''将基金信息写入Excel'''
#     titles = ['基金代码', '基金名称', '日期', '万份收益', '近5年回报率']
#     file_name = '货币基金筛选.csv'
#     with open(file_name, 'w', newline='', encoding='utf-8') as f:
#         writer = csv.DictWriter(f, fieldnames=titles)
#         writer.writeheader()
#         writer.writerows(data)
#
#
#
# get_found()
