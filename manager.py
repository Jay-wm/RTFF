class Manager():

    def __init__(self, selector):
        self.selector = selector

    def get_manager_name(self):
        '''获取当前基金经理名称'''
        manager_name = self.selector.xpath('//tbody/tr[1]/td[3]/a/text()')[0]
        return manager_name


    def get_manage_time(self):
        '''获得基金经理任职时长'''
        manage_time = self.selector.xpath('//tbody/tr[1]/td[4]/text()')[0]
        return manage_time


    def get_manage_reward(self):
        '''获得基金经理任职回报'''
        manage_reward = self.selector.xpath('//tbody/tr[1]/td[5]/text()')[0]
        return manage_reward
