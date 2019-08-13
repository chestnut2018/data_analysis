#测试git

import requests
from requests import RequestException
from lxml import etree
from time import sleep
import pymysql
conn = pymysql.connect('localhost','root','123456','work')
cur = conn.cursor()
class Boss:
    def __init__(self):
        self.headers = {
            'Host': 'www.zhipin.com',
            'Connection': 'keep-alive',
            "Upgrade-Insecure-Requests": "1",
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Referer': 'https://www.zhipin.com/job_detail/?query=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90&city=101020100&industry=&position=',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cookie': 'lastCity=101020100; _uab_collina=156558122823317113948469; _bl_uid=XXjbnzat70kuj0oazqhCwatzdemO; sid=sem_pz_bdpc_dasou_title; __c=1565663907; __g=sem_pz_bdpc_dasou_title; __l=l=%2Fwww.zhipin.com%2F%3Fsid%3Dsem_pz_bdpc_dasou_title&r=https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fDIFkY0IWPB0KZEgsAXc-FI00000Kd7ZNC00000LvWRMc.THdBULP1doZA80K85HT3nj0snWfkg1csgv99UdqsusK15yFhnhmznAcsnj0snvm1uWT0IHYLPHFafRcLP1nsnYFaPYN7njF7PWRznWDdPHb4njw7PfK95gTqFhdWpyfqn1czPjmsPjnYrausThqbpyfqnHm0uHdCIZwsT1CEQLILIz4lpA-spy38mvqVQ1q1pyfqTvNVgLKlgvFbTAPxuA71ULNxIA-YUAR0mLFW5Hf4rjb%26tpl%3Dtpl_11534_19713_15764%26l%3D1511867677%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E6%2525A0%252587%2525E9%2525A2%252598-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253DBoss%2525E7%25259B%2525B4%2525E8%252581%252598%2525E2%252580%252594%2525E2%252580%252594%2525E6%252589%2525BE%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E6%252588%252591%2525E8%2525A6%252581%2525E8%2525B7%25259F%2525E8%252580%252581%2525E6%25259D%2525BF%2525E8%2525B0%252588%2525EF%2525BC%252581%2526xp%253Did(%252522m3224604348_canvas%252522)%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D8%26ie%3Dutf-8%26f%3D8%26tn%3D78000241_20_hao_pg%26wd%3Dbiss%25E7%259B%25B4%25E8%2581%2598%26rqlang%3Dcn%26inputT%3D9522&g=%2Fwww.zhipin.com%2F%3Fsid%3Dsem_pz_bdpc_dasou_title; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1565581230,1565604124,1565656098,1565663907; __zp_stoken__=6dd8SloYLm5EtMdxqMYCgpcRVNavrydcktflzDjM2qU1YzRDZykaGSqe4Db2AK5Qy16gH78eHnNI6x6kEkrgNcpT2Q%3D%3D; __a=79307278.1565581210.1565656098.1565663907.76.5.5.5; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1565665347'
        }
        self.proxy = 'http://111.72.199.90:35491'
        self.proxies = {
            'http':self.proxy,
            'https':self.proxy
        }
    def get_index(self,url):
        try:
            r = requests.get(url,headers=self.headers)
            #print(r.apparent_encoding)
            if r.status_code==200:
                print('请求成功')
                print(r.text)
                return r.text
            else:
                return None
        except RequestException:
            print("请求错误")

    def parse_index(self,r_text,page):
        html = etree.HTML(r_text)
        for i in range(30):#一页30条数据
            job_title = html.xpath('//*[@class="job-title"]/text()')[i] #1
            salary = html.xpath('//*[@class="red"]/text()')[i] #2
            location = html.xpath('//*[@class="info-primary"]/p/text()[1]')[i] #3
            experience = html.xpath('//*[@class="info-primary"]/p/text()[2]')[i] #4
            education = html.xpath("//li/div[@class='job-primary']/div/p/text()[last()]")[i]  #5
            company_name = html.xpath('//*[@class="info-company"]/div/h3/a/text()')[i] #6
            industry = html.xpath('//*[@class="info-company"]/div/p/text()[1]')[i] #7
            situation = html.xpath('//*[@class="info-company"]/div/p/text()[2]')[i] #8
            scale = html.xpath('//*[@class="info-company"]/div/p/text()[3]')[i] #9
            print(salary)
            print("走到这里了")
            sql = "INSERT INTO boss_1 values(null,'{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(job_title,salary,location,experience,education,company_name,industry,situation,scale)
            cur.execute(sql)
            conn.commit()
        print('第{}页内容已写入完毕'.format(page))
if __name__ == '__main__':
    boss = Boss()
    city_list = [101010100,101020100,101280100,101280600,101210100,101030100,101110100,101190400,101200100,101230200,101250100,101270100,101180100,101040100]
    for city_num in city_list:
        for num in range(1,11): # 每个城市10页
            try:
                url='https://www.zhipin.com/c{}/?query=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90&page={}&ka=page-{}'.format(city_num,num,num)
                r_text = boss.get_index(url)
                boss.parse_index(r_text,num)
            except:
                break
            sleep(2)
        sleep(3)
    print('14个城市已全部爬取完毕')
