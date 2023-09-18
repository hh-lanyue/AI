import requests

url1 = 'https://kyfw.12306.cn/otn/login/checkUser'
url2 = 'https://kyfw.12306.cn/otn/confirmPassenger/getPassengerDTOs'
url3 = 'https://kyfw.12306.cn/otn/leftTicket/submitOrderRequest'

headers = {
    'Cookie': '_uab_collina=169494702310200809903987; JSESSIONID=C11CAA0527520DC8FE185F762582431B; tk=2xHNoinPgLItxMzX5Un9f9tbvjxMweuJmeQLJq0_U1Q27h1h0; guidesStatus=off; highContrastMode=defaltMode; cursorStatus=off; _jc_save_wfdc_flag=dc; _jc_save_fromStation=%u77F3%u5BB6%u5E84%2CSJP; _jc_save_fromDate=2023-09-20; _jc_save_toStation=%u5317%u4EAC%u897F%2CBXP; BIGipServerpassport=820510986.50215.0000; route=9036359bb8a8a461c164a04f8f50b252; fo=1olhrq0iocadszqz9t9eUkYpojMggh1dksmQwRApW_wWlvwo1pCPSsrsaR7Wib-GSkzEQwbodsYFg2TWFRx1YX1QyDI19EUTtZ13ljU04YWslRxHhz2HRfYPcgLmBbtILXu8pJb8dPWmY0aKRKt8XE1ceaB3AKQfdMOYabr5hzKdGzYCaS7piA-xlwk; _jc_save_toDate=2023-09-18; BIGipServerotn=1742274826.64545.0000; uKey=10895103b37dfd7f89f481822bd259acb68c855e378f909100b1a8a88603f232',
    'Connection' : 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}
params = {
    'leftTicketDTO.train_date': '2023-09-25',
    'leftTicketDTO.from_station': 'SJP',
    'leftTicketDTO.to_station': 'BXP',
    'purpose_codes': 'ADULT'
}

data = {
    'secretStr': 'BBqwKdr9nQc9ttOqfArVqx1RUFj5idQPo%2FuWtnGBriHjFZ%2BHUOGNf4b7qbeSwaqmys6SqsiucWEe%0AFA7zf2aHHjNzBUDscI6ZjwzGnj4gl1%2FY273DaoKroXnkSKIESx93C7F9PN7DNfqsSSfWKpGVlsFQ%0AJRMWMSiegoIJ7RPSJS8iUPdrIM3h2jQxF8R7unYW29qGgxvONyBlMyh6LEbE6eykpVTlSju1FK17%0AfBszVE6WvUn%2Bl%2F%2Fr0eSVLDTzj58XPfUBW2gRV6E1K9tDW%2FJDN8xsAl9SjRFw3C32vg%2B1psukZ5aK%0ADNYt3UEjns3ZvcBswTLlyCADk8xhOQubLhtwHA%3D%3D',
    'train_date': '2023-09-20',
    'back_train_date': '2023-09-18',
    'tour_flag': 'dc',
    'purpose_codes': 'ADULT',
    'query_from_station_name': '石家庄',
    'query_to_station_name': '北京西',
    'undefined': ''
}

session = requests.session()
response = session.post(url=url, headers=headers, data=data)
print(response.text)
