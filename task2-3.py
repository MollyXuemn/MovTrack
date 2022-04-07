def getValuebycolumn(cname):
    db = pymysql.connect(host='localhost',
                     user='root',
                     password='root',
                     database='movtrack')
    cur = db.cursor()
    sql=r'select `'+cname+'`  from movtrack limit 10'
    print(sql)
    row_count = cur.execute(sql)
    for line in cur.fetchall():
        print(line)
    db.close()
    return row_count
def getValuebydetail(cname,detail):
    if cname=='debut/fin':
        sql=r'select *  from movtrack where `debut/fin` REGEXP '+detail+' limit 10'
    db = pymysql.connect(host='localhost',
                     user='root',
                     password='root',
                     database='movtrack')
    cur = db.cursor()
    sql=r'select *  from movtrack where `'+cname+'`= '+detail+' limit 10'
    print(sql)
    row_count = cur.execute(sql)
    for line in cur.fetchall():
        print(line)
    db.close()
    return row_count

def demo():
    print(1)
