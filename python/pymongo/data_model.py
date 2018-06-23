#coding: utf-8
# singleton ensure access the unique object, 
# 1. __new__: clsdict assign _instance member(None)
# 2. __call__: create instance if not exists and return
class Singleton(type):
	_instances = {}
	def __call__(cls, *args, **kwargs):
		if cls not in cls._instances:
			cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
		return cls._instances[cls]


class MetaSingleton(type):
	def __new__(meta, clsname, bases, clsdict):
		clsdict["_instance"] = None
		return super(MetaSingleton, meta).__new__(meta, clsname, bases, clsdict)

	def __call__(cls, *args, **kwargs):
		if not isinstance(cls._instance, cls):
			cls._instance = super(MetaSingleton, cls).__call__(*args, **kwargs)
		return cls._instance


class User(object): # document
	def __init__(self):
		pass

class Collection(object):
	pass

class Database(object):
	def __init__(self, db_name):
		self._db_name = db_name


class MongoMananger(object):
	__metaclass__ = MetaSingleton
	"""
	connect db:
	create, insert, delete, update:
			db, collection, document
	"""
	def __init__(self):
		self._dbs = {} # {db_name: Database}

	def connect(self, host, port):
		pass

	def insert_document(col_name):
		pass

	def find_document(col_name, condition):
		pass

