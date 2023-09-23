import sys

global_dict = {}


def init_global_dict():
    global global_dict
    global_dict['is_continue'] = True
    global_dict['is_success'] = False
    global_dict['max_buy_times'] = 5
    global_dict['max_buy_times_no_change'] = 5


def set_global_value(item_value, item_key='is_continue'):
    global global_dict
    global_dict[item_key] = item_value


def get_global_value(item_key='is_continue'):
    global global_dict
    if item_key in global_dict.keys():
        return global_dict[item_key]
    else:
        return ''


# 判断程序是否继续执行
def jud_is_continue(is_reset=False, is_continue_flag=True):
    if is_reset:
        set_global_value(is_continue_flag)
    else:
        if not is_reset and not get_global_value():
            return