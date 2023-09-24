import datetime
import json
import re
from tools.session_tool import session
from domain.url_data import url_data, headers_data
from config import config
from root.root_path import root_path
from tools import error_tools


config_data = config.read_yaml(root_path + '\\' + "config\\config.yaml")
curr_date = str(datetime.datetime.now().date())


def curr_time(mode='local'):
    if mode == 'local':
        return str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    else:
        return get_beijing_time_net().strftime('%Y-%m-%d %H:%M:%S')


# 格林尼治东八区-北京时间
def get_stand_time(inpt_date):
    stand_date_temp = datetime.datetime.strptime(inpt_date, '%Y-%m-%d')
    stand_date = stand_date_temp.strftime('%a %b %d %Y %H:%M:%S') + ' GMT+0800 (中国标准时间)'
    print(type(stand_date))
    return stand_date


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


# 获取网络北京时间
def get_beijing_time_net():
    try:
        # 获取 net_time 的 url
        beijing_time_url = url_data.get('beijing_time_url')
        params = {'api': 'mtop.common.getTimestamp'}
        response = session.get(beijing_time_url, headers=headers_data, params=params)
        # 获取 net_time 返回的结果
        receive_date = json.loads(response.text)
        # 拿到时间戳
        time_stamp = receive_date['data']['t']
        if re.match('\\d{13}', time_stamp):
            time_stamp_temp = float(time_stamp)
            time_stamp_temp /= 1000.0
            # 将秒级时间戳转换为datetime对象
            time_curr = datetime.datetime.fromtimestamp(time_stamp_temp)
            # 东八区时区
            time_zone = datetime.timezone(datetime.timedelta(hours=8))
            time_result = time_curr.replace(tzinfo=time_zone)
            # 返回结果
            return time_result
    except Exception as e:
        error_tools.record_error('', e)
        return get_beijing_time_local()


# 获取本地北京时间
def get_beijing_time_local():
    # 东八区时区
    time_zone = datetime.timezone(datetime.timedelta(hours=8))
    time_curr = datetime.datetime.now(time_zone)
    # 返回结果
    return time_curr


# 车票开售时间
def get_ticket_sale_time():
    # 东八区时区
    time_zone = datetime.timezone(datetime.timedelta(hours=8))
    # 车票发售时间
    time_sale_content = config_data['custom']['ticket_sale_time']
    time_sale_temp = datetime.datetime.strptime(time_sale_content, "%Y-%m-%d %H:%M:%S")
    # 将取到的售票时间设置时区
    time_sale = time_sale_temp.replace(tzinfo=time_zone)
    return time_sale


# 得到还有多久启动抢票程序-秒级别
def get_buy_ticket_diff(time_mode='net'):
    # 售票时间
    sale_time = get_ticket_sale_time()
    # 当前时间
    if time_mode == 'net':
        current_time = get_beijing_time_net()
    else:
        current_time = get_beijing_time_local()
    # 计算时间差
    time_diff = sale_time - current_time
    time_diff_seconds = time_diff.total_seconds()

    # 返回时间差
    return time_diff_seconds, get_wait_time(time_diff_seconds)


# 判断是否开始抢票
def is_begin_buy_ticket(time_mode='net'):
    time_diff_seconds, _ = get_buy_ticket_diff(time_mode=time_mode)
    if time_diff_seconds <= 0:
        return True
    else:
        return False
