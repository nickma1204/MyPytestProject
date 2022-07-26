import os

# 获取绝对路径
# p1 = os.path.abspath('../testcases/test_currentweather.py')
# print(p1)
#
# p2 = os.path.abspath('.')
# print(p2)

# 魔法变量 __file__，变量的值在不同情况下是不一样的
# 表示当前文件
# fp = __file__
# print(fp)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 路径拼接, 定位到对应文件的根目录

DATA_DIR = os.path.join(BASE_DIR,'datas')

CASE_DIR = os.path.join(BASE_DIR, 'testcases')

print(DATA_DIR)
print(CASE_DIR)
