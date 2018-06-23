class Meta(type):
	def __new__(meta, name ,bases, clsdict):
		print clsdict['__slots__']
		clsdict['__slots__'] = ('a', 'b')
		return super(Meta, meta).__new__(meta, name, bases, clsdict)

	def hello(cls):
		print "meta hello", cls

class ClsWithSlot(object):
	__metaclass__ = Meta
	__slots__ = ("a", )

print ClsWithSlot.__mro__
ClsWithSlot.hello()
c = ClsWithSlot()
# c.hello()
c.a = 1
print dir(c)
c.b = 2
print c.a