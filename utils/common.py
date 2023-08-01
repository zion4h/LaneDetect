import os
import yaml


# 查看系统变量
def get_os_keys():
    [print(x, "=", os.environ[x]) for x in os.environ.keys()]


# 读取配置
def get_config(cfg_path):
    config_dict = dict()
    with open(cfg_path, 'rb') as f:
        date = yaml.safe_load_all(f)
        for d in date:
            for k in d:
                print(k, d[k])
                config_dict[k] = d[k]
    return config_dict
