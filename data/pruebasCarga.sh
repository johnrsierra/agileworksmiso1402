#Caso 1

httperf --server siscupos-dev.herokuapp.com --uri /siscupos/coordinacion/optimizador/ --rate 20 --num-conns 500 --export-file txt,tmp/siscupos

benchgraph --ff txt --fn /tmp/siscupos --exporter httperf

#Caso 2

httperf --server siscupos-dev.herokuapp.com --uri /siscupos/coordinacion/optimizador/ --rate 50 --num-conns 750 --export-file txt,tmp/siscuposdos

benchgraph --ff txt --fn /tmp/siscuposdos --exporter httperf
