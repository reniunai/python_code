"""可变长度参数"""


def key_word_args(id, **kwargs):
    print(kwargs, type(kwargs))
    print("id: ", id)
    print(kwargs['name'])
    print(kwargs['score'])
    

key_word_args(8888, name="zhang", age=123, score=100.0)