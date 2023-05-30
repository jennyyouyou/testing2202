#@coding=utf-8
import csv
def ReadCsv(filename):#'../test_data/login_testcase.csv'
    li=[]
    with open(filename,'r+',encoding='utf-8')  as f:
        r=csv.reader(f)
        for c in r:
            if c[0]!='caseid':
                li.append(c)
    return(li)


