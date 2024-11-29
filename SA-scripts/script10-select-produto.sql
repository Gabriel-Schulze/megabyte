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