import datetime
import pytz
from tools.session_tool import session
from domain.url_data import url_data, headers_data
from config import config
from root.root_path import root_path


config_data = config.read_yaml(root_path + '\\' + "config\\config.yaml")
curr_date = str(datetime.datetime.now().date())


def curr_time():
    return str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


# 格林尼治东八区-北京时间
def get_stand_time(inpt_date):
    stand_date_temp = datetime.datetime.strptime(inpt_date, '%Y-%m-%d')
    stand_date = stand_date_temp.strftime('%a %b %d %Y %H:%M:%S') + ' GMT+0800 (中国标准时间)'
    return stand_date


# 获取网络北京时间
def get_beijing_time_net():
    beijing_time_url = url_data.get('beijing_time_url')
    # params = {'time.asp': ''}
    response = session.get(beijing_time_url, headers=headers_data)
    return ''


# 获取本地北京时间
def get_beijing_time_local():
    beijing_zone = pytz.timezone('Asia/Shanghai')
    beijing_time = datetime.datetime.now(beijing_zone)
    return beijing_time


# 根据剩余时间设置循环等待时间
def get_wait_time(time_diff):
    # 按时间差定义每一轮循环等待时间
    #   如果剩余时间大于等于 1小时-循环等待时间为 20分钟
    #   如果剩余时间大于等于 5分钟 且小于 40分钟-循环等待时间为 5分钟
    #   如果剩余时间大于等于 1分钟 且小于 5分钟-循环等待时间为 1分钟
    #   如果剩余时间大于等于 0分钟 且小于 1分钟-循环等待时间为 0.0003分钟
    if time_diff >= 60 * 60:
        time_wait = 20 * 60
    elif 5 * 60 <= time_diff < 40 * 60:
        time_wait = 5 * 60
    elif 1 * 60 <= time_diff < 5 * 60:
        time_wait = 1 * 60
    else:
        time_wait = 0.0003 * 60
    return time_wait


# 得到还有多久启动抢票程序-秒级别
def get_buy_ticket_diff(time_mode = 'local'):
    # 定义循环等待的时间-默认60秒
    time_wait = 60 * 1000
    # 车票发售时间
    ticket_sale_time_content = config_data['custom']['ticket_sale_time']
    ticket_sale_format_time_format = datetime.datetime.strptime(ticket_sale_time_content, "%Y-%m-%d %H:%M:%S")
    beijing_zone = pytz.timezone('Asia/Shanghai')
    ticket_sale_format_time = beijing_zone.localize(ticket_sale_format_time_format)
    # 当前时间
    if time_mode == 'local':
        current_time = get_beijing_time_local()
    else:
        current_time = get_beijing_time_net()
    # 计算时间差
    time_diff = ticket_sale_format_time - current_time
    time_diff_seconds = time_diff.total_seconds()

    # 返回时间差
    return time_diff_seconds, get_wait_time(time_diff_seconds)


# 判断是否开始抢票
def is_begin_buy_ticket(time_mode='local'):
    time_diff_seconds, _ = get_buy_ticket_diff(time_mode=time_mode)
    if time_diff_seconds <= 0:
        return True
    else:
        return False


