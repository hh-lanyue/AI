import config


# 设置配置文件路径
data = config.read_yaml("config/config.yaml")
# 读取配置文件信息
get_tickets_data = {
    'leftTicketDTO.train_date': data['query']['train_date'],
    'leftTicketDTO.from_station': data['query']['from_station'],
    'leftTicketDTO.to_station': data['query']['to_station'],
    'purpose_codes': data['query']['purpose_codes']
}
