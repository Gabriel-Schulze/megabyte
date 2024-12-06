from utils import get_connection


def create_subcategoria(descricao,categoria):
    conn = get_connection()
    cursor = conn.cursor()
    query = "insert tb_subcategoria (ds_subcategoria,id_categoria) VALUES(%s,%s)"
    cursor.execute(query,(descricao,categoria))
    conn.commit()
    cursor.close()
    conn.close()

def read_subcategoria(categoria):
    conn = get_connection()
    cursor = conn.cursor()
    query = "select * from tb_subcategoria where id_categoria = %s"
    cursor.execute(query, (categoria,))
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def read_subcategoriaByName(categoria):
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * from tb_subcategoria WHERE ds_subcategoria = %s"
    cursor.execute(query, (categoria,))
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result


def update_subcategoria(id_subcategoria,descricao,categoria):
    conn = get_connection()
    cursor = conn.cursor()
    query = "update tb_subcategoria SET ds_subcategoria=%s,id_categoria = %s WHERE id_subcategoria = %s"
    cursor.execute(query, (descricao,categoria,id_subcategoria))
    conn.commit()
    cursor.close()
    conn.close()

def delete_subcategoria(id_subcategoria):
    conn = get_connection()
    cursor = conn.cursor()
    query = "delete from tb_subcategoria WHERE id_subcategoria = %s"
    cursor.execute(query, (id_subcategoria,))
    conn.commit()
    cursor.close()
    conn.close()
