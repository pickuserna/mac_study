# coding: utf-8
import sys
sys.path.append("/usr/local/lib/python2.7/site-packages")
from mongoengine import *

from user_model import User

# this is how to insert an object into mongo through mongoengine
def main():
	# regist_connection()
	# connect("orm_db", host="127.0.0.1", port=27017)
	register_connection("orm_db", "alias_orm_db")
	connect("orm_db")
	# print User.objects
	for u in User.objects:
		print u.name


def insert_users():
	user = User(email="changchangge123@qq.com", name="changchangge123").save()

if __name__ == "__main__":
	main()


