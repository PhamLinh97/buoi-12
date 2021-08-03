from utils import *
from utils_db import *

L = diemthithpt.select().where(diemthithpt.is_run == 0)

for row in L:
	row.is_run = 1
	row.save()

	sbd = row.sbd
	toan,van,anh = get_score(sbd)
	print(sbd)
	row.toan = toan
	row.van = van
	row.anh = anh
	row.save()
