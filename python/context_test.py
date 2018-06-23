#-*- coding:utf-8 -*-
class C(object):
	def __init__(self):
		print "init C"

	def __enter__(self):
		print "enter C"
		return self

	def __exit__(self, *args, **kwargs):
		print "leave C"

	def run(self):
		print "run"

with C() as c:
	c.run()
	print "C"

# 编辑者：闫龙
class Open(object):
    def __init__(self,filename,mode,encoding): #在实例化Open的时候传入文件名称,打开方式,编码格式
        self.filename = filename
        self.mode = mode
        self.encoding = encoding
        #使用系统函数open()传入相应打开文件所需的参数,将文件句柄传递给self.file
        self.file = open(filename, mode)#,mode=mode,encoding=encoding)#这里我总感觉是在作弊
    def read(self):#自己定义read方法
    	print "read "
        return self.file.read()#返回self.file文件句柄read()的值

    # def write(self,Context):#自己定义write方法
        # self.file.write(Context+"\n")#使用self.file文件句柄write方法将内容写入文件
        # print(Context,"已写入文件",self.filename)

    # 利用__getattr__(),Attr系列中的getattr,当对象没有找到Open中传递过来的名字时,调用此方法
    # def __getattr__(self, item):
        # return getattr(self.file,item)#返回self.file文件句柄中,被对象调用,切在Open类中没有的名字
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        print("文件已经关闭")

# MyFile = Open("a.txt","w+","utf8")
# MyFile.write("Egon is SomeBody")
# MyFile.close()
# MyFile = Open("a.txt","r+","utf8")
# print(MyFile.read())
# MyFile.seek(0)
# print(MyFile.readline())
# MyFile.close()

with Open("a.txt","r+", "utf-8")  as  egon:
    print(egon.read())
    pass