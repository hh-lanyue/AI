def write_content_to_file(file_path, content, is_cls=False):
    if is_cls:
        mode = 'w'
        fill_content = ''
    else:
        mode = 'a'
        fill_content = '\n'
    file_write = open(file_path, mode=mode, encoding='UTF-8')
    file_write.write(content)
    file_write.write(fill_content)
    file_write.close()


def read_file(file_path):
    file_read = open(file_path, mode='r', encoding='UTF-8')
    content = file_read.read()
    file_read.close()
    return content