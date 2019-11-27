import lxml.html

'''
xpath用法
'''

html='''
<table cellspacing="0" cellpadding="0">
<tbody>
<tr>
<td width="10%" nowrap="" style="padding-bottom: 5px;">数量: 1</td>
<td width="90%" align="right" nowrap="" style="padding-right: 5px;"></td>
</tr>
</tbody>
</table>
'''

doc=lxml.html.fromstring(html)

numList=doc.xpath('//td[@style="padding-bottom: 5px;" and @nowrap="" and not(@align="right")]/text()')

'''
获取文本
//标签1[@属性1="属性值1"]/标签2[@属性2="属性值2"]/.../text()

获取属性值
//标签1[@属性1="属性值1"]/标签2[@属性2="属性值2"]/.../@属性n
单斜杠是从根目录去匹配
双斜杠是从任意位置去匹配
'''

def parse():
	'''
		将html文件中的内容，使用xpath进行提取

	'''

	#读取文件中的内容
	f=open("./xpath.html",'r',encoding="utf-8")
	s=f.read()#读取内容
	selector=lxml.html.fromstring(s)
	h1=selector.xpath('//div[@class="post"]/h1[@class="postTitle"]/a/text()')
	#获取到的数据时一个list类型
	print(h1)
	#解析div下所有p内容
	p=selector.xpath('//div[@class="postBody"]/div[@id="cnblogs_post_body"]/p')
	length=len(p)
	for x in p:
		print(x.xpath('text()'))
	#解析a标签下的href属性值
	#
	href=selector.xpath('//div[@class="postBody"]/div[@id="cnblogs_post_body"]/h6/a/@href')
	#解析a标签
	a=selector.xpath('//div[@class="postBody"]/div[@id="cnblogs_post_body"]/h6/a')
	print(a)
	print(a[0].xpath('text()'))
	print(href[0])

	#获取p标签的最后一个内容
	p=selector.xpath('//div[@class="postBody"]/div[@id="cnblogs_post_body"]/p[last()]/text()')
	print(p[0])
	# print(selector)
	# <a href="http://www.pythoner.cn/home/blog/author/pythonercn/">pythonercn</a>
	f.close()
parse()