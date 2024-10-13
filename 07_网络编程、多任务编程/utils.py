def decode_data(bytes_arr: bytes) -> str:
    """自动尝试不同的字符集进行解码

    :param bytes_arr: 字节数组
    :return: 字符串
    """
    try:
        msg = bytes_arr.decode("UTF-8")
    except Exception as e:
        msg = bytes_arr.decode("GBK")
        
    return msg