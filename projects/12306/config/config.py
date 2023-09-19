import yaml


# 读取 config.yaml 配置文件
def read_yaml(file_path):
    with open(file_path, "r", encoding='UTF-8') as config_file:
        return yaml.safe_load(config_file)
