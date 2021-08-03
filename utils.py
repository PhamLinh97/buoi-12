import requests
from peewee import *
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
	instance = diemthithpt(sbd = sbd, toan = toan, van = van, anh = anh)
	instance.save()
	return toan,van,anh

# if __name__=="__main__":
# 	sbd = '02000001'
# 	toan,van,anh = get_score(sbd)