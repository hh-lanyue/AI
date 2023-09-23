from config import config_path


# 记录错误信息
def record_train_key(message):
    # 记录错误信息
    file_write = open(config_path.file_train_key, 'w', encoding='UTF-8')
    file_write.write(message)
    file_write.close()


def get_train_key():
    # 获取提交车票订单时需要的 train_key
    file_train_key = open(config_path.file_train_key, 'r', encoding="UTF-8")
    train_key = file_train_key.read()
    file_train_key.close()
    return train_key


def record_train_list(train_item, is_cls=False):
    if is_cls:
        mode = 'w'
    else:
        mode = 'a'
    # 记录错误信息
    file_write = open(config_path.file_train_list, mode, encoding='UTF-8')
    file_write.write(train_item)
    file_write.write('\n')
    file_write.close()