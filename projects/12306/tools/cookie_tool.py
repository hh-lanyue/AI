from config import config_path


# 写 cookie 函数
def write_cookie(cookie_info, is_first=False):
    # 读取原 cookie 信息
    # 用来判断用户是否是重新登录，如果是，则清除掉旧的 cookie
    if is_first:
        cookie_dict = {}
    else:
        cookie_dict = load_cookie()
    cookie_list = cookie_info.split(';')
    for cookie_item in cookie_list:
        cookie = cookie_item.split('=')
        cookie_dict[cookie[0]] = cookie[1]
    # 将更新后的 cookie 写入文件
    file_write = open(config_path.file_cookie, 'w', encoding='UTF-8')
    # 拿到字典个数
    cookie_nums = len(cookie_dict)
    # 字典计数器，最后一次写入时，不可以写入 ';'
    cookie_sign = 0
    for cookie_key, cookie_value in cookie_dict.items():
        cookie_sign = cookie_sign + 1
        file_write.write(cookie_key)
        file_write.write('=')
        file_write.write(cookie_value)
        if cookie_nums != cookie_sign:
            file_write.write(';')
    # 写完关闭文件
    file_write.close()


def set_cookie(response, is_first=False):
    if 'Set-Cookie' in response.headers:
        need_set_cookie = response.headers['Set-Cookie']
        write_cookie(need_set_cookie, is_first)


# 读 cookie 函数
def load_cookie():
    # 定义存放 cookie 的字典
    cookie_dict = {}
    # 读取 cookie 文件中的信息
    file_read = open(config_path.file_cookie, 'r', encoding='UTF-8')
    file_content = file_read.read()
    file_read.close()
    # 将 cookie 文件中的内容转为字典类型
    cookie_list = file_content.split(';')
    if len(file_content) == 0:
        return {}
    # 遍历 cookie_key
    for cookie_item in cookie_list:
        cookie = cookie_item.split('=')
        cookie_dict[cookie[0]] = cookie[1]
    # 返回 cookie 字典
    return cookie_dict


def get_cookie():
    # 读取 cookie 文件中的信息
    file_read = open(config_path.file_cookie, 'r', encoding='UTF-8')
    file_content = file_read.read()
    file_read.close()
    return file_content