use db_megabyte;

create table tb_produto(
	cd_produto tinyint not null,
    ds_produto varchar(45) not null,
    vl_produto decimal(8,2) not null,
    qt_produto smallint not null,
    id_subcategoria tinyint not null,
    id_fornecedor tinyint not null,
    id_usuario tinyint not null,
    
    constraint pk_produto primary key(cd_produto),
    constraint fk_produto_subcategoria foreign key(id_subcategoria) references tb_subcategoria(id_subcategoria),
    constraint fk_produto_fornecedor foreign key(id_fornecedor) references tb_fornecedor(id_fornecedor),
    constraint fk_produto_usuario foreign key(id_usuario) references tb_usuario(id_usuario),

)