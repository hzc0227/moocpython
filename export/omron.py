# -*- coding = utf-8 -*-
# @author:   hanzhihchao7
# @date:     2023/2/14 10:29
# @File:     omron.py
# @Software: PyCharm


from pymongo import MongoClient
import xlwt
from config import MongoConfig

mongo_client = MongoClient(MongoConfig.URL, MongoConfig.PORT)
my_db = mongo_client['omron']
my_col = my_db['faq_202302']

datas = my_col.find({}, {
    '_id': 0,
    'question': 1,
    'answer': 1,
    'question_category': 1,
    'product_category': 1,
    'qa_href': 1
})

cols = ('问题分类', '问题', '回答', '产品分类', '问答链接')
workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('sheet1', cell_overwrite_ok=True)

for i in range(0, 5):
    worksheet.write(0, i, cols[i])
row = 1

for data in datas:
    # print(data)
    data = list(data.values())
    for col in range(0, len(cols)):
        worksheet.write(row, col, data[col])
    row += 1

workbook.save('D:\\omron_faq_202302.xls')
