import config


# 设置配置文件路径
data = config.read_yaml("config/config.yaml")
# 获取提交车票订单时需要的 train_key
file_train_key = open('result/train_key.txt', 'r', encoding="UTF-8")
train_key = file_train_key.read()
file_train_key.close()

# 读取配置文件信息
buy_pre_submit_order_data = {
    'secretStr': train_key,
    'train_date': data['buy']['pre']['train_date'],
    'back_train_date': '2023-09-18',
    'tour_flag': 'dc',
    'purpose_codes': data['buy']['pre']['purpose_codes'],
    'query_from_station_name': data['buy']['pre']['query_from_station_name'],
    'query_to_station_name': data['buy']['pre']['query_to_station_name'],
    'undefined': ''
}