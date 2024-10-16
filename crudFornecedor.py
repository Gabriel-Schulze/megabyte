from utils import get_connection


def create_fornecedor(nome,cnpj,endereco,telefone):
    conn = get_connection()
    cursor = conn.cursor()
    query = "insert tb_fornecedor (nm_empresa,nr_cnpj,ds_endereco,nr_telefone) VALUES(%s,%s,%s,%s)"
    cursor.execute(query,(nome,cnpj,endereco,telefone))
    conn.commit()
    cursor.close()
    conn.close()

def read_fornecedor():
    conn = get_connection()
    cursor = conn.cursor()
    query = "select * from tb_fornecedor"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def update_fornecedor(id_fornecedor,nome,cnpj,endereco,telefone):
    conn = get_connection()
    cursor = conn.cursor()
    query = "update tb_fornecedor SET nm_empresa=%s,nr_cnpj = %s,ds_endereco = %s,nr_telefone  = %s WHERE id_fornecedor = %s"
    cursor.execute(query, (nome,cnpj,endereco,telefone,id_fornecedor))
    conn.commit()
    cursor.close()
    conn.close()

def delete_fornecedor(id_fornecedor):
    conn = get_connection()
    cursor = conn.cursor()
    query = "delete from tb_fornecedor WHERE id_fornecedor = %s"
    cursor.execute(query, (id_fornecedor,))
    conn.commit()
    cursor.close()
    conn.close()
