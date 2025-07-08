import sqlite3


def check_exist(cursor, keyword):
    sql_check = f"""
    select  DISTINCT beauty.keyword, beauty.one,beauty.one,beauty.two,beauty.three,beauty.four,beauty.five,
    beauty.six,beauty.seven,beauty.eight,beauty.nine,beauty.ten,a.age, s.shape 
    from beauty, age as a,shape as s
    join age on beauty.keyword = age.keyword
    join shape on beauty.keyword = shape.keyword
    where beauty.keyword = ?
    GROUP BY beauty.keyword
    ;
    """
    cursor.execute(sql_check,(keyword,))
    result = cursor.fetchall()
    return result


def save_data2db(keyword, dic):


    conn = sqlite3.connect('data_analyze.db')
    cursor = conn.cursor()


    beauty_count = dic['beauty']
    beauty_count.insert(0, keyword)
    dic_age = [int(dic['age'])]
    dic_age.insert(0, keyword)
    dic_shape = [dic['face_shape']]
    dic_shape.insert(0, keyword)


    param_shape = list(dic_shape)
    print("param_shape: ", param_shape)
    params_beauty = list(beauty_count)
    print("params_beauty: ",params_beauty)
    params_age = list(dic_age)
    print("params_age: ", params_beauty)

    # 建表
    sql = '''
    CREATE TABLE IF NOT EXISTS beauty(
        id           INTEGER    PRIMARY KEY,
        detect_time  TEXT       DEFAULT      CURRENT_TIMESTAMP,
        keyword      TEXT,
        no_face      INTEGER    DEFAULT 0,
        one			 INTEGER    DEFAULT 0,
        two          INTEGER    DEFAULT 0,
        three        INTEGER    DEFAULT 0,
        four         INTEGER    DEFAULT 0,
        five         INTEGER    DEFAULT 0,
        six          INTEGER    DEFAULT 0,
        seven        INTEGER    DEFAULT 0,
        eight        INTEGER    DEFAULT 0,
        nine         INTEGER    DEFAULT 0,
        ten          INTEGER    DEFAULT 0
    );
    '''
    cursor.execute(sql)

    sql_age = '''
    CREATE TABLE IF NOT EXISTS age(
        id           INTEGER    PRIMARY KEY,
        detect_time  TEXT       DEFAULT      CURRENT_TIMESTAMP,
        keyword      TEXT,
        age          INTEGER    DEFAULT 0    
    );
    '''
    cursor.execute(sql_age)

    sql_shape = """
    CREATE TABLE IF NOT EXISTS shape(
        id           INTEGER    PRIMARY KEY,
        detect_time  TEXT       DEFAULT      CURRENT_TIMESTAMP,
        keyword      TEXT,
        shape     VARCHAR(10)    DEFAULT 0
    );
    """

    cursor.execute(sql_shape)

    results = check_exist(cursor, keyword)

    for result in results:
        print("db_result: ",result)


    if not results:
        # beauty 的插入

        sql = """
        insert into beauty(keyword, no_face, one, two, three, four, five, six, seven, eight, nine, ten) values(?,?,?,?,?,?,?,?,?,?,?,?);
        """
        cursor.execute(sql, params_beauty)

        ### age 的插入


        sql_age = """
        insert into age(keyword, age) values(?,?);
        """

        cursor.execute(sql_age, params_age)


        ### shape的插入



        sql_shape = """
        insert into shape(keyword, shape) values(?,?);
        """

        cursor.execute(sql_shape, param_shape)
        conn.commit()

    elif results:
        # beauty 的更新

        sql = """
        UPDATE beauty
        SET no_face = no_face + ?,
            one = one + ?,
            two = two + ?,
            three = three + ?,
            four = four + ?,
            five = five + ?,
            six = six + ?,
            seven = seven + ?,
            eight = eight + ?,
            nine = nine + ?,
            ten = ten + ?
        WHERE beauty.keyword = ?
        ;
        """
        print("update beauty:", params_beauty[1:] + params_beauty[:1])
        cursor.execute(sql, params_beauty[1:] + params_beauty[:1])

        ### age 的更新


        sql_age = """
        update age
        set age = (age + ?)/2
        where age.keyword = ?
        ;
        """

        cursor.execute(sql_age, params_age[1:] + params_age[:1])


        ### shape更新

        sql_shape = """
        update shape
        set shape = ?
        where shape.keyword = ?
        ;
        """

        cursor.execute(sql_shape, param_shape[1:] + param_shape[:1])
        conn.commit()




