# 命令行启用代理
set http_proxy=http://127.0.0.1:8888
set https_proxy=https://127.0.0.1:8888
# 命令行关闭代理
set http_proxy=
set https_proxy=

# 更新 pip
python -m pip install --upgrade pip

# 安装
pip install torch
pip install torchvision
==注意== torch 与 torchvision 要对应版本

如果有 GPU 装 CUDA-11.3

