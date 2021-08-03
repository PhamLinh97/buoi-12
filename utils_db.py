from peewee import *

host = 'localhost'
db_name = 'buoi12'
db_user = 'root'
db_pass = ''
db = MySQLDatabase(db_name,host=host,user = db_user, passwd = db_pass)


class diemthithpt(Model):
	sbd = CharField()
	toan = FloatField()
	van = FloatField()
	anh = FloatField()
	is_run = IntegerField()
	class Meta:
		database=db

if __name__=="__main__":
	diemthithpt.create_table()