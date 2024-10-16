from utils import get_connection


def create_produto(cd_produto,descricao,valor,quantidade,subcategoria,fornecedor):
    conn = get_connection()
    cursor = conn.cursor()
    query = "insert tb_produto VALUES(%s,%s,%s,%s,%s,%s)"
    cursor.execute(query,(cd_produto,descricao,valor,quantidade,subcategoria,fornecedor))
    conn.commit()
    cursor.close()
    conn.close()

def read_produto():
    conn = get_connection()
    cursor = conn.cursor()
    query = "select * from tb_produto"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def update_produto(cd_produto,descricao,valor,quantidade,subcategoria,fornecedor):
    conn = get_connection()
    cursor = conn.cursor()
    query = "update tb_produto SET ds_produto=%s,vl_produto=%s,qt_produto=%s,id_subcategoria=%s,id_fornecedor=%s WHERE cd_produto = %s"
    cursor.execute(query, (descricao,valor,quantidade,subcategoria,fornecedor,cd_produto))
    conn.commit()
    cursor.close()
    conn.close()

def delete_produto(cd_produto):
    conn = get_connection()
    cursor = conn.cursor()
    query = "delete from tb_produto WHERE cd_produto = %s"
    cursor.execute(query, (cd_produto,))
    conn.commit()
    cursor.close()
    conn.close()
