#!/usr/bin/python
# -*- coding: UTF-8 -*-
#1.读取excel
import xlrd
fname='reflect.xls'
bk=xlrd.open_workbook(fname)
shxrange=range(bk.nsheets)
try:
    sh=bk.sheet_by_name('Sheet1')
except:
    print('no sheet in %s named Sheet1' % fname)
#获取行数
nrows=sh.nrows
#获取列数
ncols=sh.cols
print('nrows %d,ncols %d % (nrows,ncols))
#获取第一行第一列数据
cell_value=sh.cell_value(1,1)

row_list=[]
#获取各行数据
for i in range(1,nrows):
    row_data=sh.row_value(i)
	row_list.append(row_data)
#写入EXCEL
from pyExcelerator import *
w=Workbook() #创建一个工作簿
ws=w.add_sheet('hey') #创建一个工资表
ws.write(0,0,'bit') #在1行1列写入bit
ws.write(0,1,'huang')
ws.write(1,0,'xuan')
w.save('mini.xls')#保存
#3.再举个自己写的读写Excel的例子 读取reflect.xls中的某些信息进行处理后写入mini.xls文件中。
#-*- coding: utf8 -*-
import xlrd
from pyExcelerator import *
  
w = Workbook() 
ws = w.add_sheet('Sheet1') 
 
fname = "reflect.xls"
bk = xlrd.open_workbook(fname)
shxrange = range(bk.nsheets)
try:
 sh = bk.sheet_by_name("Sheet1")
except:
 print "no sheet in %s named Sheet1" % fname
 
nrows = sh.nrows
ncols = sh.ncols
print "nrows %d, ncols %d" % (nrows,ncols)
  
cell_value = sh.cell_value(1,1)
#print cell_value
row_list = []
mydata = []
for i in range(1,nrows):
 row_data = sh.row_values(i)
 pkgdatas = row_data[3].split(',')
 #pkgdatas.split(',')
 #获取每个包的前两个字段
 for pkgdata in pkgdatas:
  pkgdata = '.'.join((pkgdata.split('.'))[:2])
  mydata.append(pkgdata)
 #将列表排序
 mydata = list(set(mydata))
 print mydata
 #将列表转化为字符串
 mydata = ','.join(mydata)
 #写入数据到每行的第一列
 ws.write(i,0,mydata)
 w.save('mini.xls')
#4.现在我需要根据Excel文件中满足特定要求的apk的md5值来从服务器获取相应的apk样本，就需要这样做：

#-*-coding:utf8-*-
import xlrd
import os
import shutil
  
fname = "./excelname.xls"
bk = xlrd.open_workbook(fname)
shxrange = range(bk.nsheets)
try:
 #打开Sheet1工作表
 sh = bk.sheet_by_name("Sheet1")
except:
 print "no sheet in %s named Sheet1" % fname
#获取行数
nrows = sh.nrows
#获取列数
ncols = sh.ncols
#print "nrows %d, ncols %d" % (nrows,ncols)
#获取第一行第一列数据
cell_value = sh.cell_value(1,1)
#print cell_value
  
row_list = []
#range(起始行,结束行)
for i in range(1,nrows):
 row_data = sh.row_values(i)
 if row_data[6] == "HXB":
  filename = row_data[3]+".apk"
  #print "%s %s %s" %(i,row_data[3],filename)
  filepath = r"./1/"+filename
  print "%s %s %s" %(i,row_data[3],filepath)
  if os.path.exists(filepath):
   shutil.copy(filepath, r"./myapk/")
　
