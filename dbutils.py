import sqlite3



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
    params_beauty = tuple(beauty_count)
    print("params_beauty: ",params_beauty)
    params_age = tuple(dic_age)
    print("params_age: ", params_beauty)


    ### beauty的建表和插入
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

    sql = """
    insert into beauty(keyword, no_face, one, two, three, four, five, six, seven, eight, nine, ten) values(?,?,?,?,?,?,?,?,?,?,?,?);
    """
    cursor.execute(sql, params_beauty)

    ### age 的建表和插入

    sql_age = '''
    CREATE TABLE IF NOT EXISTS age(
        id           INTEGER    PRIMARY KEY,
        detect_time  TEXT       DEFAULT      CURRENT_TIMESTAMP,
    	keyword      TEXT,
        age          INTEGER    DEFAULT 0    
    );
    '''
    cursor.execute(sql_age)
    sql_age = """
    insert into age(keyword, age) values(?,?);
    """

    cursor.execute(sql_age, params_age)


    ### faceshape的建表和插入

    sql_shape = """
    CREATE TABLE IF NOT EXISTS shape(
        id           INTEGER    PRIMARY KEY,
        detect_time  TEXT       DEFAULT      CURRENT_TIMESTAMP,
    	keyword      TEXT,
    	shape     VARCHAR(10)    DEFAULT 0
    );
    """

    cursor.execute(sql_shape)

    sql_shape = """
    insert into shape(keyword, shape) values(?,?);
    """

    cursor.execute(sql_shape, param_shape)
    conn.commit()


