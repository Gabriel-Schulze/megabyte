from utils import get_connection


def create_usuario(nome,cpf,telefone,perfil,email,senha):
    conn = get_connection()
    cursor = conn.cursor()
    query = "insert tb_usuario (nm_usuario,nr_cpf,nr_telefone,ds_perfil,ds_email,ds_senha) VALUES(%s,%s,%s,%s,%s,%s)"
    cursor.execute(query,(nome,cpf,telefone,perfil,email,senha))
    conn.commit()
    cursor.close()
    conn.close()

def read_usuario():
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT id_usuario, nm_usuario, nr_telefone, ds_email, nr_cpf FROM tb_usuario ORDER BY id_usuario LIMIT 10"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def read_usuarioById(id):
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT nm_usuario,nr_cpf,nr_telefone,ds_perfil,ds_email,ds_senha FROM tb_usuario WHERE id_usuario = %s"
    cursor.execute(query,(id,))
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result


def read_usuarioByName(nome):
    conn = get_connection()
    cursor = conn.cursor()
    query = f"""SELECT  id_usuario, nm_usuario, nr_telefone, ds_email, nr_cpf  FROM tb_usuario WHERE nm_usuario LIKE "%{nome}%" """
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def verify_usuario(email,senha):
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT ds_perfil, nm_usuario FROM tb_usuario WHERE ds_email = %s AND ds_senha = %s"
    cursor.execute(query, (email,senha))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def update_usuario(id_usuario,nome,cpf,perfil,telefone,email,senha):
    conn = get_connection()
    cursor = conn.cursor()
    query = "update tb_usuario SET nm_usuario=%s,nr_cpf = %s,ds_perfil = %s, nr_telefone=%s,ds_email=%s,ds_senha=%s WHERE id_usuario = %s"
    cursor.execute(query, (nome,cpf,perfil,telefone,email,senha,id_usuario))
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
