from utils import get_connection


def create_fornecedor(nome,cnpj,endereco,telefone,id_usuario):
    conn = get_connection()
    cursor = conn.cursor()
    query = "insert tb_fornecedor (nm_empresa,nr_cnpj,ds_endereco,nr_telefone,id_usuario) VALUES(%s,%s,%s,%s,%s)"
    cursor.execute(query,(nome,cnpj,endereco,telefone,id_usuario))
    conn.commit()
    cursor.close()
    conn.close()

def read_fornecedor():
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT id_fornecedor, nm_empresa, nr_cnpj, ds_endereco, nr_telefone FROM tb_fornecedor ORDER BY id_fornecedor LIMIT 10"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def read_fornecedorById(id):
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT nm_empresa, nr_cnpj, ds_endereco, nr_telefone FROM tb_fornecedor WHERE id_fornecedor = %s"
    cursor.execute(query,(id,))
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def read_fornecedorByName(nome):
    conn = get_connection()
    cursor = conn.cursor()
    query = f"""SELECT id_fornecedor, nm_empresa, nr_cnpj, ds_endereco, nr_telefone FROM tb_fornecedor WHERE nm_empresa LIKE "%{nome}%" """
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
