import lxml.html
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def get_page_sources(url, condition):
    '''初始化driver'''
    driver = webdriver.Chrome('./chromedriver')
    driver.get(url)
    try:
        WebDriverWait(driver, 90).until(EC.present_in_element((By.ID, condition)))
    except Exception as _:
        print('网页加载太慢了，不等了。')

    # 得到排行榜页面源代码并返回
    page_source = driver.page_source
    selector = lxml.html.fromstring(page_source)
    return selector


def get_url(selector, num):
    '''获取排行榜第num个基金页面的网址'''
    address = '//*[@id="fund_list"]/tbody/tr[' + str(num+1) + ']/td[2]/a/@href'
    found_url = selector.xpath(address)[0]
    return found_url

def save_date(data):
    '''将基金信息写入Excel'''

    # 靠
    titles = ['基金代码', '基金名称', '成立日期', '基金规模(亿元)']
    file_name = '债券基金筛选test.csv'
    with open(file_name, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=titles)
        writer.writeheader()
        writer.writerows(data)