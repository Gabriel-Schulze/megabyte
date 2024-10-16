from utils import get_connection

def read_categoria():
    conn = get_connection()
    cursor = conn.cursor()
    query = "select * from tb_categoria"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result
