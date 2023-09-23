from config import config_path
from tools import global_variable_manger_tool as global_manger


# 记录错误信息
def record_error(message, e=''):
    # 记录错误信息
    file_write = open(config_path.file_error_info, 'w', encoding='UTF-8')
    file_write.write(message)
    file_write.close()
