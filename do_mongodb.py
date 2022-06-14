#!/usr/bin/env python
# coding=utf-8

'''
操作mongodb
'''
import pymongo
from pymongo import MongoClient

# 连接mongodb,参数可选
# client = MongoClient(host='localhost', port=27017)
client = MongoClient()

# 指定数据库
db = client['mymog']

# 指定数据库中的集合
collection = db['students']

stua = {
    'name': 'tom',
    'age': 18,
    'sex': '男',
}

stub = {
    'name': 'jack',
    'age': 21,
    'sex': '男',
}

stuc = {
    'name': 'lucy',
    'age': 20,
    'sex': '女',
}
stud = {
    '语文': 90,
    '数学': 100,
    '英语': 91,
}

# 插入数据,单条,多条
# collection.insert_one(stua)
# collection.insert_many([stub, stuc])
# collection.insert_one(stud)


# 查询
# 查询单条数据
result = collection.find_one({'name': 'lucy'})

# 查询多条数据,输出为集合
results = collection.find({'sex': '男'})
for rs in results:
    print(rs)

'''
符号含义示例
$lt小于{'age': {'$lt': 20}}
$gt大于{'age': {'$gt': 20}}
$lte小于等于{'age': {'$lte': 20}}
$gte大于等于{'age': {'$gte': 20}}
$ne不等于{'age': {'$ne': 20}}
$in在范围内{'age': {'$in': [20, 23]}}
$nin不在范围内{'age': {'$nin': [20, 23]}}
'''

print('年龄小于21的数据')
results = collection.find({'age': {'$lt': 21}})
for rs in results:
    print(rs)

'''
符号含义示例示例含义
$regex匹配正则表达式{'name': {'$regex': '^M.*'}}name以M开头
$exists属性是否存在{'name': {'$exists': True}}name属性存在
$type类型判断{'age': {'$type': 'int'}}age的类型为int
$mod数字模操作{'age': {'$mod': [5, 0]}}年龄模5余0
$text文本查询{'$text': {'$search': 'Mike'}}text类型的属性中包含Mike字符串
$where高级条件查询{'$where': 'obj.fans_count == obj.follows_count'}自身粉丝数等于关注数
'''

print('name以t开头的数据')
results = collection.find({'name': {'$regex': '^l.*'}})
for rs in results:
    print(rs)

# 统计表中有多少条数据
# count = collection.find().count()
# print(count)
# 统计指定值得条数
count = collection.count_documents({'name': 'tom'})
print(count)

print('按姓名排序:ASCENDING升序,DESCENDING降序')
results = collection.find().sort('name', pymongo.DESCENDING)
for rs in results:
    # print(rs['name'])  # 注意筛选时检索含有空值的字段将不显示结果
    print(rs)

print('偏移')
results = collection.find().sort('name', pymongo.ASCENDING).skip(1)
for rs in results:
    print(rs['name'])  # 使用偏移去除部分数据后可用
    # print(rs)

print('提取')
results = collection.find().sort('name', pymongo.DESCENDING).skip(1).limit(2)
for rs in results:
    print(rs['name'])  # 使用偏移去除部分数据后可用
    # print(rs)

print('更新')
condition = {'name': 'jack'}
st = collection.find_one(condition)
st['age'] = 28
result = collection.update(condition, st)
print(result)

print('更新2')
condition = {'name', 'tom'}
st = collection.find_one(condition)
st['age'] = 30
result = collection.update_one(condition, {'$set': st})
print(result)
print(result.matched_count, result.modified_count)
