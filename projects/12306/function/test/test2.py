import requests

url = 'https://kyfw.12306.cn/otn/passport?redirect=/otn/login/userLogin'
url_full = 'https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=2023-09-25&leftTicketDTO.from_station=SJP&leftTicketDTO.to_station=BXP&purpose_codes=ADULT'
headers = {
    #'Cookie': '_uab_collina=169484625613968223555056; JSESSIONID=E9375A871563FF8B70BCC8BB2AF137B5; tk=y0DWLxeSyBK2ODaxd2Dt31pPSI1aPDtRSFVCUB0Tptwhuh1h0; route=6f50b51faa11b987e576cdb301e545c4; guidesStatus=off; highContrastMode=defaltMode; cursorStatus=off; BIGipServerpassport=837288202.50215.0000; _jc_save_fromStation=%u77F3%u5BB6%u5E84%2CSJP; _jc_save_toDate=2023-09-16; _jc_save_wfdc_flag=dc; BIGipServerpool_passport=48497162.50215.0000; BIGipServerotn=1557725450.50210.0000; _jc_save_toStation=%u5317%u4EAC%u897F%2CBXP; _jc_save_fromDate=2023-09-25; uKey=10895103b37dfd7f89f481822bd259ac8eb399559bf1ee936f72f5b9d2b9cec0; fo=yo3expa8mezay9hsgTsDTK1a_2aK41KGhOqFIFNSf1C5c8W_Ec7L39sr6lgSkpDxWSoeNRDpJgk8vSfR0HDYqjcW4lkth_ImhaW2Z0v1-4OZMdgzfKiixQKsaEHPYxleRz0e0Wfxu6zGRdbyUOE-cczkA9NKDtXFct_jGEkDPxzA3ipBS1dOBrrKqTs',
    'Connection' : 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}
params = {
    'leftTicketDTO.train_date': '2023-09-25',
    'leftTicketDTO.from_station': 'SJP',
    'leftTicketDTO.to_station': 'BXP',
    'purpose_codes': 'ADULT'
}

session = requests.session()
response = session.get(url=url, headers=headers)
print(response.headers['Set-Cookie'])
