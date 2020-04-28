def get_found():
    '''将每个基金的源代码放到数组中'''
    Found_body_list = driver.find_elements_by_xpath('//*[@id="dbtable"]/tbody/tr')

