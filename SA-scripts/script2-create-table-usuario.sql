use db_megabyte;

create table tb_usuario(
	id_usuario tinyint not null auto_increment,
    nm_usuario varchar(45) not null,
    nr_cpf varchar(14) not null,
    nr_telefone varchar(15) not null,
    ds_perfil enum("admin","padrao") not null,
    ds_email varchar(100) not null,
    ds_senha varchar(45) not null,
    
    constraint pk_usuario primary key(id_usuario)

)