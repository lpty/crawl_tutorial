from lagou.https import Http
from lagou.parse import Parse
from lagou.setting import headers as hd
from lagou.setting import cookies as ck
import time
import logging
logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)s Process%(process)d:%(thread)d %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='diary.log',
                    filemode='a')


def getInfo(url, para):
    """
    获取信息
    """
    generalHttp = Http()
    htmlCode = generalHttp.post(url, para=para, headers=hd, cookies=ck)
    generalParse = Parse(htmlCode)
    pageCount = generalParse.parsePage()
    info = []
    for i in range(1, pageCount+1):
        print('第%s页' % i)
        para['pn'] = str(i)
        htmlCode = generalHttp.post(url, para=para, headers=hd, cookies=ck)
        generalParse = Parse(htmlCode)
        info = info + getInfoDetail(generalParse)
        time.sleep(2)
    return info


def getInfoDetail(generalParse):
    """
    信息解析
    """
    info = generalParse.parseInfo()
    return info


def processInfo(info, para):
    """
    信息存储
    """
    logging.error('Process start')
    try:
        title = 'companyName,companyType,companyStage,companyLabel,companySize,companyDistrict,' \
                'positionType,positionEducation,positionAdvantage,positionSalary,positionWorkYear\n'
        file = open('%s.txt' % para['city'], 'a')
        file.write(title)
        for p in info:
            line = str(p['companyName']) + ',' + str(p['companyType']) + ',' + str(p['companyStage']) + ',' + \
                   str(p['companyLabel']) + ',' + str(p['companySize']) + ',' + str(p['companyDistrict']) + ',' + \
                   str(p['positionType']) + ',' + str(p['positionEducation']) + ',' + str(p['positionAdvantage']) + ',' +\
                   str(p['positionSalary']) + ',' + str(p['positionWorkYear']) + '\n'
            file.write(line)
        file.close()
        return True
    except:
        logging.error('Process except')
        return None


def main(url, para):
    """
    主函数逻辑
    """
    logging.error('Main start')
    if url:
        info = getInfo(url, para)             # 获取信息
        flag = processInfo(info, para)             # 信息储存
        return flag
    else:
        return None


if __name__ == '__main__':
    kdList = [u'数据分析']
    cityList = [u'广州', u'深圳']
    url = 'https://www.lagou.com/jobs/positionAjax.json'
    for city in cityList:
        print('爬取%s' % city)
        para = {'first': 'true','pn': '1', 'kd': kdList[0], 'city': city}
        flag = main(url, para)
        if flag: print('%s爬取成功' % city)
        else: print('%s爬取失败' % city)
