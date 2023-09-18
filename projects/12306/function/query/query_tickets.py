import json
from function.session.session_manger import session
from domain.url_data import url_data
from domain.headers_data import headers_data
from domain.get_tickets_data import get_tickets_data


class query_tickets:
    # 构造函数
    def __init__(self):
        # 登录前校验地址
        self.query_ticket_url = url_data.get('query_ticket_url')
        # 读取 Cookie
        self.my_cookie = ''

    # 从文件加载 cookie
    def load_cookie(self):
        file_cookie = open('config/cookie.txt', 'r', encoding="UTF-8")
        self.my_cookie = file_cookie.read()
        return self.my_cookie

    # 登录前校验
    def get_tickets(self):
        self.load_cookie()
        # 发送登录请求
        response = session.get(self.query_ticket_url, headers=headers_data, params=get_tickets_data)
        if response.status_code == 200:
            try:
                res_data = json.loads(response.text)
            except Exception as e:
                # 出现异常，抛出错误
                print('查询异常')
                file_error = open('config/error.html', 'w', encoding='UTF-8')
                file_error.write(response.text)
                print(e.args)
            else:
                # 如果没有异常且成功，则保存 cookie
                if res_data['status'] and res_data['httpstatus'] == 200:
                    print('查询火车票成功')
                    if res_data['data']['flag'] == '1':
                        file_query = open('result/train_list.txt', 'w', encoding='UTF-8')
                        train_list = res_data['data']['result']
                        for train in train_list:
                            file_query.write(train + '\n')
                        file_query.close()
                        # 注意放开 BEG
                        for train in res_data['data']['result']:
                            li = list(train.split("|"))
                            if li[3] == 'G654':
                                train_key = li[0]
                                file_train_key = open('result/train_key.txt', 'w', encoding='UTF-8')
                                file_train_key.write(train_key)
                                file_train_key.close()
                        # 注意放开 END
                else:
                    print('查询火车票未成功')
        else:
            print('查询火车票失败')

    def init_query(self):
        self.get_tickets()