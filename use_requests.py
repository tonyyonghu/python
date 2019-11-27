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
# get_html(url)
# get_book()
#http://search.dangdang.com/?key=python&act=input
#用%格式化
def format_str():
	name="张三"
	print("%s" % name)
	num=23.3444
	print("%.3f" % num)
	num=34
	print("%04d" % num)
	tt=(1,2,3,4,5,5,6,7)
	print("%s" % str(tt))

format_str()

def format_str_2():
	#使用位置
	print("欢迎您,{0},{1},''''{1}说".format('张三',"好久不仅"))
	#使用名称
	print("您好，{username},您的编号是{num}".format(username="张三",num=54))

	data={
		'username':'历史',
		'num':87
	}
	print("您好，{username},您的编号是{num}".format(**data))

	#格式化元组
	point=(3,4,5,6,7,9)
	print("位置坐标：{0[0]}:{0[1]}".format(point))

	#格式化类
	user=User("历史",98)
	# print(user.show())
	print(user)

class User(object):
	def __init__(self,username,age):
		self.username = username
		self.age = age

	def show(self):
		return "用户名：{self.username},年龄{self.age}".format(self=self)

	def __str__(self):
		return self.show()
format_str_2()

# https://www.bilibili.com/video/av68337879?p=9