# coding: utf-8
import sys
sys.path.append("/usr/local/lib/python2.7/site-packages")
from mongoengine import *


class User(Document):
	email = StringField(required=True)
	name = StringField(max_length=30)
	meta = {"db_alias": "alias_orm_db"}


class Post(Document):
	content = StringField(max_length=100)
