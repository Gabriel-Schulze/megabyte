from utils import get_connection


def create_usuario(nome,cpf,telefone,email,senha):
    conn = get_connection()
    cursor = conn.cursor()
    query = "insert tb_usuario (nm_usuario,nr_cpf,nr_telefone,ds_email,ds_senha) VALUES(%s,%s,%s,%s,%s)"
    cursor.execute(query,(nome,cpf,telefone,email,senha))
    conn.commit()
    cursor.close()
    conn.close()

def read_usuario():
    conn = get_connection()
    cursor = conn.cursor()
    query = "select * from tb_usuario"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def update_usuario(id_usuario,nome,cpf,telefone,email,senha):
    conn = get_connection()
    cursor = conn.cursor()
    query = "update tb_usuario SET nm_usuario=%s,nr_cpf = %s, nr_telefone=%s,ds_email=%s,ds_senha=%s WHERE id_usuario = %s"
    cursor.execute(query, (nome,cpf,telefone,email,senha,id_usuario))
    conn.commit()
    cursor.close()
    conn.close()

def delete_usuario(id_usuario):
    conn = get_connection()
    cursor = conn.cursor()
    query = "delete from tb_usuario WHERE id_usuario = %s"
    cursor.execute(query, (id_usuario,))
    conn.commit()
    cursor.close()
    conn.close()
