import requests
from lxml import html

HEADERS={
	"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Mobile Safari/537.36"
}

def spider(sn):
	#爬取京东的图书数据
	url="https://search.jd.com/Search?keyword={0}&enc=utf-8&wq={0}&pvid=8e25e4743acc478aab9b3b2fc5f3a1ea".format(sn,sn)
	response=requests.get(url=url,headers=HEADERS)
	response.encoding="utf-8"
	#获取html数据
	html_doc=response.text
	#获取xpath对象
	selector=html.fromstring(html_doc)

	#找到列表的集合
	ul_list=selector.xpath('//div[@id="J_goodsList"]/ul/li')
	print(len(ul_list))
	for li in ul_list:

		#解析对应的内容，标题
		#价格
		price=li.xpath('div[@class="gl-i-wrap"]/div[@class="p-price"]/strong/i/text()')
		#链接
		link=li.xpath('div[@class="gl-i-wrap"]/div[@class="p-img"]/a/@href')
		#书名
		title=li.xpath('div[@class="gl-i-wrap"]/div[@class="p-img"]/a/@title')
		print(title)
		#出版社
		publish=li.xpath('div[@class="gl-i-wrap"]/div[@class="p-shopnum"]/a/@title')
		publish="京东自营" if len(publish)==0 else publish[0]
		# print(publish)
	# print(url)

if __name__=="__main__":
	spider("python")