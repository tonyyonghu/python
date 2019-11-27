import requests
import lxml.html

HEADERS={
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
}
def get_book():
	'''获取书的方法'''
	url="http://search.dangdang.com/"
	res=requests.get(url,params={
		'key':'python',
		'act':'input'
		})
	#json的方式获取数据
	#res.json()
	#res.status_code
	print(res.encoding)#文件编码
	#HTTP状态码
	#2x
	#4x 404 403
	#500
	# print(res.text)
def get_html(url):
	response=requests.get(url=url,headers=HEADERS)
	# print(response.text)

url="http://search.dangdang.com/?key=python&act=input"
get_html(url)
get_book()
#http://search.dangdang.com/?key=python&act=input