import re

import requests


def Daily_Laugh():
    Laugh_url = 'https://www.qiushibaike.com/text/'
    sess = requests.Session()
    res = sess.get(Laugh_url).content
    #print res
    Laugh_pattern = r'(.*?)'
    Laugh_list = re.findall(Laugh_pattern, res,re.S)
    Laugh = Laugh_list[0].replace('', '\n')
    return Laugh