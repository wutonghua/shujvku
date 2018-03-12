1.把excel数据写入数据库
#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pymysql 
import xlrd
conn= pymysql.connect(
        host='123.232.38.99',
        port = 3306,
        user='root',
        passwd='Jth2016',
        db ='zbap',
	charset='utf8'
        )
cur=conn.cursor()     
fname = "E:/lpthw/dxc.xlsx"
bk = xlrd.open_workbook(fname)
shxrange = range(bk.nsheets)
try:
    sh = bk.sheet_by_name("Sheet1")
except:
    print "no sheet in %s named Sheet1" % fname
nrows=sh.nrows
ncols=sh.ncols
print "nrows %d, ncols %d" % (nrows,ncols)
cell_value=sh.cell_value(1,1)
row_list=[]
for i in range(1,nrows):
    row_data=sh.row_values(i)
    row_list.append(row_data)
for line in range(len(row_list)):
    cur.execute("INSERT INTO zbap_dxc (age,weight,body_fat,body_quality_param,basal_metabolic_rate,inter_cell_fluid,extra_cell_fluid,bone_mineral_content,skel_muscle,trunk_muscle,count_val,user_id,name) VALUE(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(row_list[line][1],row_list[line][11],row_list[line][10],row_list[line][6],row_list[line][2],
    row_list[line][8],row_list[line][9],row_list[line][3],row_list[line][5],row_list[line][7],row_list[line][12],'11','admin'))
cur.close()
conn.commit()
conn.close()
2.把数据库内容导入到excel表格
# -*- coding: UTF-8 -*-
import sys 
reload(sys)  
sys.setdefaultencoding('utf8')   
import pymysql
conn= pymysql.connect(
        host='123.232.38.99',
        port = 3306,
        user='root',
        passwd='Jth2016',
        db ='dadev',
		charset='utf8'
        )
cursor=conn.cursor()
sql="select disea_name from repository_disease " 
cursor.execute(sql)
rows = cursor.fetchall()

with open('jibingmc.txt','w') as f:
    for i in rows:
        f.write(i[0])
f.close()
conn.commit()
cursor.close()
conn.close()

		


    
    

    





    
