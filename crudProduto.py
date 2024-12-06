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
    query = """
        SELECT
            p.cd_produto,
            p.ds_produto,
            p.vl_produto,
            c.ds_categoria,
            s.ds_subcategoria
        FROM
            tb_produto p
        INNER JOIN tb_subcategoria s 
        ON (p.id_subcategoria = s.id_subcategoria)
        INNER JOIN tb_categoria c
        ON (c.id_categoria = s.id_categoria)
        ORDER BY p.cd_produto
    """
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def read_produtoById(id):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        SELECT 
            cd_produto, 
            ds_produto, 
            vl_produto,
            qt_produto, 
            id_subcategoria,
            id_fornecedor,
            id_usuario 
        FROM tb_usuario 
        WHERE id_usuario = %s
    """
    cursor.execute(query,(id,))
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def read_produtoByName(nome):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        SELECT
            p.cd_produto,
            p.ds_produto,
            p.vl_produto,
            c.ds_categoria,
            s.ds_subcategoria
        FROM
            tb_produto p
        INNER JOIN tb_subcategoria s 
        ON (p.id_subcategoria = s.id_subcategoria)
        INNER JOIN tb_categoria c
        ON (c.id_categoria = s.id_categoria)
        WHERE p.ds_produto = %s
        ORDER BY p.cd_produto
    """
    cursor.execute(query,(nome,))
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
