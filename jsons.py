import json
import datetime
def parse():
	d={
	    'name':"python书籍",
	    'sale_price':43.45,
	    'origin_price':66,
	    'pub_date':datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
	    'store':['京东',"淘宝"],
	    'author':('张三','李四','王五'),
	    'is_valid':True,
	    'is_sale':False,
	    'meta':{
	    	'isbn':'abc-123',
	    	'pages':300
	    },
	    'desc':None
	}
	rest=json.dumps(d,indent=4,sort_keys=True) #indent=4缩进
	print(rest)
parse()


'''
将python转化成json对象

'''
def python_to_json():
	d={
		'name':'python书籍'
	}
	rest=json.dumps(d)
	print(rest)
	print(type(rest))
python_to_json()

'''
将json转化成python
'''
def json_to_python():
	data='{"name":"python书籍","origin_price":66,"pub_date":"2019-11-27","store":["京东","淘宝"],"author":["张三","李四","王五"],"is_valid":true,"is_sale":false,"meta":{"isbn":"abc-123","pages":300},"desc":null}'
	rest=json.loads(data)
	print(rest)
	print(rest['name'])

json_to_python()

'''
从文件中读取json数据
'''
def json_to_python_fromfile():
	f=open("./book.json",'r',encoding="utf-8")
	s=f.read()
	print(type(s))
	rest=json.loads(s)
	print(rest['name'])
	f.close()

json_to_python_fromfile()