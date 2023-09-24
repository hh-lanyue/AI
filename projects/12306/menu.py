import time
from function.buy.buy import buy
from function.query.query_tickets import query_tickets
from tools import global_variable_manger_tool as global_manger
from tools import time_tool


# 购票任务
def exec_task():
    # 登录
    # my_login = login()
    # my_login.init_login()
    # 查票
    my_query_tickets = query_tickets()
    my_query_tickets.init_query()
    # 买票
    my_buy = buy()
    my_buy.init_buy()


# 开始抢票入口
def buy_ticket():
    # 定义统一管理的全局变量
    global_manger.init_global_dict()
    # 如果[购票没有成功且尝试购票次数没有超过最大次数-max_buy_times]则一直循环准备购票
    while not global_manger.get_global_value('is_success') and global_manger.get_global_value('max_buy_times') > 0:
        # 如果没有到车票发售时间则一直循环等待
        while not time_tool.is_begin_buy_ticket(time_mode='net'):
            time_diff, time_wait = time_tool.get_buy_ticket_diff(time_mode='net')
            print('当前时刻 ', time_tool.curr_time(), '距离车票发售时间还有 ', time_diff, ' 秒，程序继续休眠 ', time_wait, '秒')
            time.sleep(time_wait)
        # 统计购票次数
        global_manger.set_global_value(item_key='max_buy_times', item_value=global_manger.get_global_value('max_buy_times') - 1)
        print('[第' + str(global_manger.get_global_value('max_buy_times_no_change') - global_manger.get_global_value('max_buy_times')) + '次]当前时刻 ', time_tool.curr_time(), ' 程序开始为您自动化购票, 请稍后......')
        # 开始购票
        exec_task()


buy_ticket()
