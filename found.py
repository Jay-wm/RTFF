class Found():
    '''表示基金的类'''

    def __init__(self, selector1, selector2):
        '''初始化属性page_source'''
        self.selector1 = selector1
        self.selector2 = selector2

    def get_name(self):
        '''获取基金名称'''
        found_name = self.selector1.xpath('//*[@id="body"]/div[12]/div/div/div[1]/div[1]/div/text()')[0]
        return found_name

    def get_ticker(self):
        '''获得基金代码'''
        found_ticker = self.selector1.xpath('//*[@class="ui-num"]/text()')[0]
        return found_ticker

    def get_date_of_establishment(self):
        '''获取基金成立日期'''
        found_date_establishment0 = self.selector1.xpath('//*[@id="body"]/div[12]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[1]/text()')[0]
        found_date_establishment = found_date_establishment0.replace('：', '')
        return found_date_establishment

    def get_scale(self):
        '''获取基金规模，并去掉单位等干扰信息得到具体数值（亿元）'''
        # 获取初始基金规模
        found_scale0 = self.selector1.xpath('//*[@id="body"]/div[12]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[1]/td[2]/text()')[0]
        # 剔除基金规模前面的冒号
        found_scale1 = found_scale0.replace('：', '')
        # 将基金规模（带单位）转换成数组
        found_scale1_list = list(found_scale1)
        # 初始化基金规模（浮点型数值）数组
        found_scale_list = []
        # 获得基金规模（浮点型数值）数组
        for i in range(len(found_scale1_list) - 14):
            found_scale_list.append(found_scale1_list[i])
        # 将基金规模（浮点型数值）数组转换成浮点型数据
        found_scale = float(''.join(found_scale_list))
        return found_scale

    def get_manager_name(self):
        '''获取当前基金经理名称'''
        manager_name = self.selector2.xpath('//tbody/tr[1]/td[3]/a/text()')[0]
        return manager_name

    def get_manage_time(self):
        '''获得基金经理任职时长'''
        manage_time = self.selector2.xpath('//tbody/tr[1]/td[4]/text()')[0]
        return manage_time

    def get_manage_reward(self):
        '''获得基金经理任职回报'''
        manage_reward = self.selector2.xpath('//tbody/tr[1]/td[5]/text()')[0]
        return manage_reward
