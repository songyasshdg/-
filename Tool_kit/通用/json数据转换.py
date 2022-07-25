# 导入 json 库
import json

# 要传输的 Python 数据对象
python_data = {
    "name": "唐僧",
    "age": 18,
    "height": 180.0,
    "male": True,
    "students": {
        "name": "孙悟空",
        "age": 500
    },
    "friends": ["如来佛祖", "观音菩萨"],
    "other_students": [
        {"name": "猪八戒", "age": 300},
        {"name": "沙和尚", "age": 200}
    ],
    "salary": None
}

# 转换为 JSON 格式字符串，并输出。
# 添加 ensure_ascii=False 是为了将中文字符使用 utf-8 编码。
json_str = json.dumps(python_data, ensure_ascii=False)
print("数据类型：", type(json_str))
print("数据内容：", json_str)
