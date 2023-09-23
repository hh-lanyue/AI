import datetime


curr_date = str(datetime.datetime.now().date())
curr_time = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


# 格林尼治东八区-北京时间
def get_stand_time(inpt_date):
    stand_date_temp = datetime.datetime.strptime(inpt_date, '%Y-%m-%d')
    stand_date = stand_date_temp.strftime('%a %b %d %Y %H:%M:%S') + ' GMT+0800 (中国标准时间)'
    return stand_date
