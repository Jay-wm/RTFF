'''债券基金筛选'''
from found import Found
from manager import Manager
import function

def start():
    '''开始筛选'''
    # 在天天基金网里面的货币基金筛选，
    # 以“1000元起”，
    # “成立年限大于七年”进行初步筛选后，
    # 在“自定义时间在2015/6/1-2016/2/29之间的大盘下跌的这段时间”收益情况进行排序后的网址
    url = 'http://fund.eastmoney.com/daogou/#dt0;ftzq;rs;sd2015-06-01;ed2016-02-29;pr;cp;rt;tp;rk;se;nx71;scdiy;stdesc;pi1;pn20;zfdiy;shlist'

    # 获取在chromedriver.exe中得到的源代码经初始化后的selector
    selector1 = function.get_page_sources(url, '//*[@id="fund_list"]')

    # 获取基金的详细网页网址
    found_url_list = function.get_url(selector1)

    # 通过基金规模进行再次筛选
    for i in range(20):
        selector2 = function.get_page_sources(found_url_list[i], '//tbody/tr/td[3]/[@href]')
        found_class = Found(selector2)
        found_scale = found_class.get_scale()
        found_

        # 首先得到基金规模


        #



start()
