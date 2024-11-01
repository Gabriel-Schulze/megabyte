use db_megabyte;

create table tb_fornecedor(
	id_fornecedor tinyint not null auto_increment,
    nm_empresa varchar(45) not null,
    nr_cnpj varchar(15) not null,
    ds_endereco varchar(100) not null,
    nr_telefone varchar(15) not null,
    id_usuario tinyint not null,
    
    constraint pk_fornecedor primary key(id_fornecedor),
    constraint fk_fornecedor_usuario foreign key(id_usuario) references tb_usuario(id_usuario)
)