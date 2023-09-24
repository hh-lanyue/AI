global_dict = {}


def init_global_dict():
    global global_dict
    # 记录本次程序的执行状态
    global_dict['is_continue'] = True
    # 记录抢票是否成功
    global_dict['is_success'] = False
    # 规定剩余最大购票尝试次数-会随实际购票次数耳边
    global_dict['max_buy_times'] = 5
    # 规定最大购票尝试次数-不会变
    global_dict['max_buy_times_no_change'] = 5
    # 由于程序执行也需要时间，所以设置一个开始购票时间的误差范围
    global_dict['mistake'] = 0.8


def set_global_value(item_key, item_value):
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
        set_global_value(item_key='is_continue', item_value=is_continue_flag)
    else:
        if not is_reset and not get_global_value():
            return