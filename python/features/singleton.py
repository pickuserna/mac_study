# coding: utf-8
# 1. meta class
# 2. decorator
# 3. 

#2. decorator
def singleton(cls):
	def wrapper(*args, **kwargs):
		if not (hasattr(cls, "_instance") and isinstance(cls._instance, cls)):
			cls._instance = cls(*args, **kwargs)
		return cls._instance
	return wrapper

def singleton_dec(cls):
	_instance = {} # cannot change outter variable reference
	def get_instance(*args, **kwargs):
		if not (_instance and isinstance(_instance, cls)):
			_instance[cls] = cls(*args, **kwargs)
		return _instance
	return get_instance

@singleton_dec
class A(object):
	def __init__(self, a):
		self._a = a 

obj_a1 = A(1)
obj_a2 = A(2)
print obj_a1 == obj_a2


# 3. 

