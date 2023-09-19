from config import config_path


# 记录错误信息
def record_log(message):
    # 记录错误信息
    file_write = open(config_path.file_log, 'a', encoding='UTF-8')
    file_write.write(message)
    file_write.write('\n')
    file_write.close()