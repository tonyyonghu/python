import requests
from lxml import html

HEADERS={
	"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Mobile Safari/537.36"
}

def spider(sn):
	"""爬取当当网的数据"""
	url="http://search.dangdang.com/?key={sn}&act=input".format(sn=sn)
	#获取HTML内容
	
	data=requests.get(url=url,headers=HEADERS).text

	#xpath对象
	selector=html.fromstring(data)
	ul_list=selector.xpath('//div[@id="search_nature_rg"]/ul/li')

	print(ul_list)
	for li in ul_list:
		#标题
		title=li.xpath('a/@title')
		#购买链接
		link=li.xpath('a/@href')
		#价格
		price=li.xpath('p[@class="price"]/span[@class="search_now_price"]/text()')
		price=price[0].replace("¥","")
		# print(price)
		# print("*"*20)
		#商家
		#
		store=li.xpath('div[@class="lable_label"]/span[@class="new_lable"]/span[@class="new_lable1"]/text()')
		store="当当自营" if len(store) == 0 else store[0]
		print(store)
spider("python")