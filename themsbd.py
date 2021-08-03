import requests
from peewee import *
from peewee import chunked
from utils_db import *
from requests.models import codes

def get_score(sbd):
	# sbd = '02000001'
	url = f'https://diemthi.vnanet.vn/Home/SearchBySobaodanh?code={sbd}&nam=2021'

	headers = {
		'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/96.0.230 Chrome/90.0.4430.230 Safari/537.36',
		'X-Requested-With' : 'XMLHttpRequest'
	}

	res = requests.get(url, headers = headers).json()
	try:
		toan = res['result'][0]['Toan']
		van = res['result'][0]['NguVan']
		anh = res['result'][0]['NgoaiNgu']
	except:
		toan = -1
		van = -1
		anh = 1
	instance = diemthi(sbd = sbd, toan = toan, van = van, anh = anh)
	instance.save()
	return toan,van,anh

# toan,van,anh = get_score(sbd)



data_source = [
	{
		'sbd' : f'020{i}'
	}
	for i in range (10000,89000)
]

for batch in chunked(data_source,10000):
	diemthithpt.insert_many(batch).execute()