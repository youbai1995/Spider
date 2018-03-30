# -*- coding : UTF-8 -*-

import json
import jsonpath
import requests
import datetime
import queue

def getCity(city):
    citydict = {
        '北京':'BJS','张家界':'DYG','大理':'DLU','丹东':'DDG', '芒市':'LUM','上海':'SHA',
        '桂林':'KWL','济南':'TNA','牡丹江':'MDG','拉萨':'LXA','广州':'CAN','贵阳':'KWE',
        '福州':'FOC','呼和浩特':'HET','铜仁':'TEN','深圳':'SZX','晋江':'JJN','太原':'TYN',
        '石家庄':'SJW','攀枝花':'PZI','武汉':'WUH','南宁':'NNG','温州':'WNZ','武夷山':'WUS',
        '威海':'WEH','长沙':'CSX','湛江':'ZHA','北海':'BHY','连云港':'LYG','无锡':'WUX','西安':'SIA',
        '沈阳':'SHE','景洪':'JHG','齐齐哈尔':'NDG','银川':'INC','重庆':'CKG','长春':'CGQ','宁波':'NGB',
        '绵阳':'MIG','延吉':'YNJ','成都':'CTU','汕头':'SWA','宜昌':'YIH','丽江':'LJG','中甸':'DIG','南京':'NKG',
        '黄山':'TXN','梅县':'MXZ','景德镇':'JDZ','包头':'BAV','昆明':'KMG','乌鲁木齐':'URC','常州':'CZX','佳木斯':'JMU',
        '黄岩':'HYN','南昌':'KHN','兰州':'LHW','烟台':'YNT','兴义':'ACX','梧州':'WUZ','厦门':'XMN','西宁':'XNN','天津':'TSN',
        '满州里':'NZH','临沂':'LYI','海口':'HAK','柳州':'LZH','南通':'NTG','井冈山':'JGS','沙市':'SHS','三亚':'SYX','保山':'BSD',
        '义乌':'YIW','大同':'DAT','九江':'JIU','杭州':'HGH','运城':'YCU','南阳':'NNY','敦煌':'DNH','锦州':'JNZ','哈尔滨':'HRB',
        '长治':'CIH','洛阳':'LYA','百色':'AEB','泸州':'LZO','青岛':'TAO','连城':'LCX','常德':'CGD','赣州':'KOW','盐城':'YNZ',
        '大连':'DLC','合肥':'HFE','宜宾':'YBP','南充':'NAO','潍坊':'WEF','珠海':'ZUH','襄樊':'XFN','安庆':'AQG','九寨沟':'JZH',
        '衢州':'JUZ','郑州':'CGO','吉林':'JIL','徐州':'XUZ','广元':'GYS','永州':'LLF'
    }
    City = citydict.get(city)#获取城市对应三字代码
    City = str(City)#转换成str形式
    return City

def getEveryDay(begin_date,end_date):
    date_list = []
    begin_date = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(end_date,"%Y-%m-%d")
    while begin_date <= end_date:
        date_str = begin_date.strftime("%Y-%m-%d")
        date_list.append(date_str)
        begin_date += datetime.timedelta(days=1)
    return date_list

def geturl(DCity,ACity,Date):
    urllist = queue.Queue()
    url = 'http://flights.ctrip.com/domesticsearch/search/SearchFirstRouteFlights?DCity1=' + DCity + "&ACity1=" + ACity + '&SearchType=S&DDate1=' + Date
    urllist.put(url)
    urllist.get()

def main(DCity,ACity,Date,maxprice):
    headers = {
        'Host' : 'flights.ctrip.com',
        'Cache-Control' : 'max-age=0',
        'Upgrade-Insecure-Requests' : '1',
        'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding' : 'gzip, deflate, sdch',
        'Accept-Language' : 'zh-CN,zh;q=0.8',
        'Cookie' : '_abtest_userid=d8acf40b-bd99-4d4c-a32a-fc629f1c7551; GUID=09031168410855693377; HotelCityID=2split%E4%B8%8A%E6%B5%B7splitShanghaisplit2018-1-26split2018-01-27split0; appFloatCnt=3; StartCity_Pkg=PkgStartCity=32; traceExt=campaign=CHNbaidu81&adid=index; adscityen=Guangzhou; Session=SmartLinkCode=U153507&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=&SmartLinkLanguage=zh; Union=OUID=title&AllianceID=5376&SID=153507&SourceID=&Expires=1518230709419; manualclose=1; DomesticUserHostCity=CAN|%b9%e3%d6%dd; __zpspc=9.14.1517629443.1517629443.1%233%7Cwww.so.com%7C%7C%7C%7C%23; _jzqco=%7C%7C%7C%7C1517625909536%7C1.1773865467.1516933714186.1517625928012.1517629443498.1517625928012.1517629443498.undefined.0.0.44.44; FD_SearchHistorty={"type":"S","data":"S%24%u5E7F%u5DDE%28CAN%29%24CAN%242018-02-15%24%u4E0A%u6D77%28SHA%29%24SHA"}; _RF1=163.177.136.73; _RSG=lqaqXMEO6B5ogqNCNdMo0A; _RDG=283d86d5305517270a304ebac2d5b88495; _RGUID=52c660e5-a1d2-4d2f-a032-5a75cc5f4ab2; Mkt_UnionRecord=%5B%7B%22aid%22%3A%22761445%22%2C%22timestamp%22%3A1517188667747%7D%2C%7B%22aid%22%3A%224897%22%2C%22timestamp%22%3A1517471270297%7D%2C%7B%22aid%22%3A%225376%22%2C%22timestamp%22%3A1517641193850%7D%5D; _ga=GA1.2.2009874240.1516933714; _gid=GA1.2.318181679.1517625909; MKT_Pagesource=PC; _bfa=1.1516933711238.47ahnf.1.1517625906849.1517641190746.14.81.212093; _bfs=1.2; _bfi=p1%3D101027%26p2%3D101027%26v1%3D81%26v2%3D80'
        }

    #url = 'http://flights.ctrip.com/domesticsearch/search/SearchFirstRouteFlights?DCity1=CAN&ACity1=SHA&SearchType=S&DDate1=2018-02-11'#测试链接
    url = 'http://flights.ctrip.com/domesticsearch/search/SearchFirstRouteFlights?DCity1=' + DCity + "&ACity1=" + ACity + '&SearchType=S&DDate1=' + Date
    response = requests.get(url,headers = headers)
    try:
        response.status_code == 200
        print('链接正常',response.status_code)
    except:
        print('链接有误',response.status_code)
    print('日期：',Date)
    demo = json.loads(response.text)
    #print(response.status_code)
    aim = jsonpath.jsonpath(demo,"$..acn")#目的地
    fn = jsonpath.jsonpath(demo,'$..fn')#航班型号
    times = jsonpath.jsonpath(demo,"$..dt")#起飞时间
    time = []
    for i in times:#筛选times中数据
        if len(i) > 1:
            time.append(i)
    #price = jsonpath.jsonpath(demo,"$..scs[0].p")#确定价格唯一元素
    price = jsonpath.jsonpath(demo,"$..fis.[:100].lp")#价格另一个确定方法
    rata = jsonpath.jsonpath(demo,"$..scs[0]..rate")#折扣
    #rt = jsonpath.jsonpath(demo,"$..scs[0]..rt")#折扣
    #print(len(aim),len(fn),len(time),len(price),len(rata))#列表长度,检测数据是否有误
    code = map(list,zip(aim,fn,time,price,rata))#将列表放入一个列表
    code = filter(lambda x:x[3]<=int(maxprice),code)#筛选价格
    #code = filter(lambda x:x[4]<=0.8,code)#通过折扣筛选列表元素
    for i in code:
        print('航班',i)

if __name__ == '__main__':
    dcity = input("出发城市：")
    acity = input("目的地：")
    DCity = getCity(dcity)
    ACity = getCity(acity)
    begin_date = input('开始时间（格式：xxxx-xx-xx）：')
    end_date = input('结束时间：(格式：xxxx-xx-xx）：')
    maxprice = input('最高价格：')
    print('行程', dcity, '-', acity)
    Date = getEveryDay(begin_date,end_date)
    for i in Date:
        main(DCity,ACity,i,maxprice)

    for i in Date:
        geturl(DCity,ACity,i)
#修改成多线程，加入数据库
#合肥-南京报错原因：无直达机票0