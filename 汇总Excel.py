# -*- coding: utf-8 -*-
#合并多个Excel表格

import xlsxwriter

import xlrd

import os

work=xlsxwriter.Workbook(r'.\汇总.xlsx') #建立一个文件

sheet=work.add_worksheet('汇总') #新建一个sheet

path='.'                      #目录(放Excel表格的目录)

file_list=os.listdir(path)

file_name='';x1=1

for file in file_list:                                #循环遍历列出所有文件名称

    if 'xlsx' in file:

        file_name = os.path.join(path,file)              #路径+文件名

    else:

        continue

    workbook=xlrd.open_workbook(file_name)            #打开第一个文件

    sheet_name=workbook.sheet_names()                #获取第一个文件的sheet名称

    for file_1 in sheet_name:                        #循环遍历每个sheet

        table=workbook.sheet_by_name(file_1)                #以名字为索引

        rows=table.nrows                                    #获取sheet行数

        clos=table.ncols                                    #获取sheet列数目

        for i in range(rows):                              #循环遍历每一行

            sheet.write_row('A'+str(x1),table.row_values(i))#获取每一行的值追加到新表

            x1+=1

    print('已完成 ' + file_name)

work.close()