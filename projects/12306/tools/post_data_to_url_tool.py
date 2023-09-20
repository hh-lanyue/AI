def post_data_to_url(post_data):
    request_args = []
    # 遍历 post 请求参数
    for key in post_data.items():
        my = "=".join(key)
        # 拼接参数
        request_args.append(my)
    # 格式化参数
    params = "?" + "&".join(request_args)
    return params
