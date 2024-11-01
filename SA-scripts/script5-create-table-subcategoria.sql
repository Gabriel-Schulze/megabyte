use db_megabyte;

create table tb_subcategoria(
	id_subcategoria tinyint not null auto_increment,
    ds_subcategoria varchar(45) not null,
    id_categoria tinyint not null,
    id_usuario tinyint not null,
    
    constraint pk_subcategoria primary key(id_subcategoria),
    constraint fk_subcategoria_categoria foreign key(id_categoria) references tb_categoria(id_categoria),
    constraint fk_subcategoria_usuario foreign key(id_usuario) references tb_usuario(id_usuario)

)