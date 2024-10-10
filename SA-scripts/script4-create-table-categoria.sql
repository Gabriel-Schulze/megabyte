use db_megabyte;

create table tb_categoria(
	id_categoria tinyint not null auto_increment,
    ds_categoria varchar(45),
    
    constraint pk_categoria primary key(id_categoria)

)