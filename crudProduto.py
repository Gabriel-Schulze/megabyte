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
            p.cd_produto, 
            p.ds_produto, 
            p.vl_produto,
            p.qt_produto,
            c.ds_categoria,
            s.ds_subcategoria,
            f.nm_empresa,
            p.id_subcategoria,
            p.id_fornecedor 
        FROM tb_produto p 
        INNER JOIN tb_subcategoria s 
        ON (p.id_subcategoria = s.id_subcategoria)
        INNER JOIN tb_fornecedor f
        ON (p.id_fornecedor = f.id_fornecedor)
        INNER JOIN tb_categoria c
        ON (s.id_categoria = c.id_categoria)
        WHERE p.cd_produto = %s
    """
    cursor.execute(query,(id,))
    result = cursor.fetchone()
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

def update_produto(codigoNovo,descricao,valor,quantidade,subcategoria,fornecedor,codigoAtual):
    conn = get_connection()
    cursor = conn.cursor()
    query = "UPDATE tb_produto SET cd_produto=%s,ds_produto=%s,vl_produto=%s,qt_produto=%s,id_subcategoria=%s,id_fornecedor=%s WHERE cd_produto = %s"
    cursor.execute(query, (codigoNovo,descricao,valor,quantidade,subcategoria,fornecedor,codigoAtual))
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
