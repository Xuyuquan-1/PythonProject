import sqlite3


def save_data2db(keyword, y_axis):
    conn = sqlite3.connect('data_analyze.db')
    cursor = conn.cursor()

    y_axis.insert(0, keyword)
    params = tuple(y_axis)
    print(params)

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
    cursor.execute(sql, params)
    conn.commit()