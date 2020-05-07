import time
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

# 筛选基金
def filter_found(found_url):
    found_page_source = get_page_sources(found_url, '//*[@class="wrapper_min"]')
    selector = lxml.html.fromstring(found_page_source)

    '''获得基金成立日期'''
    found_date_establishment0 = selector.xpath('//*[@id="body"]/div[12]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[1]/text()')[0]
    found_date_establishment = found_date_establishment0.replace('：', '')

    
    '''将获得的日期转换为以秒作单位'''
    found_date_establishment_sec = time.mktime(time.strptime(found_date_establishment, "%Y-%m-%d"))
    date = time.mktime(time.strptime('2013-1-1', "%Y-%m-%d"))

    '''通过成立日期进行第一次筛选，满足成立年限大于7年，则获取基金规模进行判断'''
    if found_date_establishment_sec < date:
        '''获取基金规模，并去掉单位等干扰信息得到具体数值（亿元）'''
        found_scale0 = selector.xpath('//*[@id="body"]/div[12]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[1]/td[2]/text()')[0]
        found_scale1 = found_scale0.replace('：', '')
        found_scale1_list = list(found_scale1)
        found_scale_list = []
        for i in range(len(found_scale1_list) - 14):
            found_scale_list.append(found_scale1_list[i])

        found_scale = float(''.join(found_scale_list))
        '''通过比较基金规模是否在5-50亿元之间进行二次筛选基金'''
        if 5.00 < found_scale < 50.00:
            found_name = selector.xpath('//*[@id="body"]/div[12]/div/div/div[1]/div[1]/div/text()')[0]
            found_ticker = selector.xpath('//*[@class="ui-num"]/text()')[0]
            found_dict =  {'基金代码': found_ticker, '基金名称': found_name, '成立日期': found_date_establishment,
                '基金规模(亿元)': found_scale}
            return found_dict
        else:
            print(format('基金规模' +found_scale0 + '不满足5-50亿要求' ))
            return 0
    else:
        print(format('基金成立日期：' + found_date_establishment + '，成立年限小于7年'))
        return 0

# 将获取的基金资料以字典形式存入CSV格式文件中
def save_data(data):
    '''将基金信息写入Excel'''
    titles = ['基金代码', '基金名称', '成立日期', '基金规模(亿元)']
    file_name = '债券基金筛选.csv'
    with open(file_name, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=titles)
        writer.writeheader()
        writer.writerows(data)

# 债券基金排行榜网址
url = 'http://fund.eastmoney.com/daogou/#dt0;ftzq;rs;sd2015-06-01;ed2016-02-29;pr;cp;rt;tp;rk;se;nx71;scdiy;stdesc;pi1;pn20;zfdiy;shlist'

# 初始化变量与基金字典数组
num = 0
i = 0
data = []

# 获得债券基金排行榜页面源代码
foundList_page_source = get_page_sources(url, '//*[@id="fund_list"]')

# 筛选出5个满足：基金规模-尽量选择规模大的，最好在5-50亿之间，规模太小容易有波动；成立年限-7年以上的债券基金
while i < 5:
    found_url = get_url(foundList_page_source, num)
    if filter_found(found_url):
        found_dict = filter_found(found_url)
        data.append(found_dict)
        i += 1
        print(i)
        num += 1
    else:
        num += 1

# 将获取的满足条件的5个基金数据进行保存     
save_data(data)
