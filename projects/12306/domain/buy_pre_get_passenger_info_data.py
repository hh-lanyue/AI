from tools import analy_key_tool


# 读取配置文件信息
def get_passenger_info_data():
    # 定义返回结果变量
    passenger_info_data = {}
    global_token = analy_key_tool.analy_global_token_to_obj()
    # 赋值请求参数
    passenger_info_data['_json_att']=''
    passenger_info_data['REPEAT_SUBMIT_TOKEN']=global_token
    # 返回结果
    return passenger_info_data
