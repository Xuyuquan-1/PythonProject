import sqlite3

def select_AgeBdata():
    """
    查询数据库中数据分析的历史记录
    :return: 包含查询结果的列表
    """
    conn = sqlite3.connect('data_analyze.db')
    cursor = conn.cursor()

    sql='select beauty.keyword,avg(age) as age_avg,avg(one + two + three + four + five + six + seven + eight + nine + ten) as beauty_avg from beauty,age where beauty.keyword=age.keyword group by beauty.keyword;'
    cursor.execute(sql)
    rows=cursor.fetchall() # 拿到所有查询结果

    cursor.close()
    conn.close()
    return rows


def select_FaceBdata():
    conn = sqlite3.connect('data_analyze.db')
    cursor = conn.cursor()
    sql='select shape,count(shape) from shape group by shape;'

    cursor.execute(sql)
    rows_Shape = cursor.fetchall()  # 拿到所有查询结果

    cursor.close()
    conn.close()
    return rows_Shape

def select_Beautydata():
    conn = sqlite3.connect('data_analyze.db')
    cursor = conn.cursor()
    sql='select beauty.keyword,two,four,six,eight,nine,ten from beauty group by beauty.keyword;'
    cursor.execute(sql)
    rows_Beauty = cursor.fetchall()  # 拿到所有查询结果

    cursor.close()
    conn.close()
    return rows_Beauty


def select_Namedata():
    conn = sqlite3.connect('data_analyze.db')
    cursor = conn.cursor()
    sql='select keyword from beauty;'
    cursor.execute(sql)
    rows_Name = cursor.fetchall()  # 拿到所有查询结果

    cursor.close()
    conn.close()
    return rows_Name

if __name__ == '__main__':
    rows_AgeB=select_AgeBdata()
    rows_Shape=select_FaceBdata()
    rows_Beauty=select_Beautydata()
    rows_Name=select_Namedata()