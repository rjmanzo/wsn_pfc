/*
PARA CORRER ESTE SCRIPT DEBEMOS EJECUTAR ESTA ACCION SOBRE LA CARPETA DEL DIRECTORIO GIT.
TENIENDO ESTE ARCHIVO INICIALIZADOR, EJECUTAMOS EL SIGUIENTE COMANDO SOBRE LA CONSOLA:

user@$ cat inicializar_db.sql | heroku psql 

*/

/*
SCRIPT DE GENERACION DE LAS PRINCIPALES VARIABLES DEL SISTEMA
*/

--Table: rol
INSERT INTO rol (rol_descrip) VALUES ('Coordinador');
INSERT INTO rol (rol_descrip) VALUES ('Router');
INSERT INTO rol (rol_descrip) VALUES ('Hoja');
--Table: nodo
INSERT INTO nodo (nod_descrip) VALUES ('Nodo_0');
INSERT INTO nodo (nod_descrip) VALUES ('Nodo_1');
INSERT INTO nodo (nod_descrip) VALUES ('Nodo_2');
INSERT INTO nodo (nod_descrip) VALUES ('Nodo_3');
INSERT INTO nodo (nod_descrip) VALUES ('Nodo_4'); 
--Table: tipo_sensor
INSERT INTO tipo_sensor (type_sen_descrip) VALUES ('Temperatura');
INSERT INTO tipo_sensor (type_sen_descrip) VALUES ('Humedad');
INSERT INTO tipo_sensor (type_sen_descrip) VALUES ('Distancia');
INSERT INTO tipo_sensor (type_sen_descrip) VALUES ('Presión');
INSERT INTO tipo_sensor (type_sen_descrip) VALUES ('Batería');
--Table:  wsn
INSERT INTO wsn (wsn_descrip) VALUES ('Prueba de Laboratorio');
INSERT INTO wsn (wsn_descrip) VALUES ('Prueba de campo Nro. 1');
INSERT INTO wsn (wsn_descrip) VALUES ('Prueba de campo Nro. 2');
--Table: sensor
INSERT INTO sensor (sen_descrip,type_sen_id) VALUES ('DHT22',1);
INSERT INTO sensor (sen_descrip,type_sen_id) VALUES ('DHT22',2);
INSERT INTO sensor (sen_descrip,type_sen_id) VALUES ('BMP183',1);
INSERT INTO sensor (sen_descrip,type_sen_id) VALUES ('MCP9808',2);
INSERT INTO sensor (sen_descrip,type_sen_id) VALUES ('GP2Y0A710K0F',3);
INSERT INTO sensor (sen_descrip,type_sen_id) VALUES ('Tensión',5);

/*
INICIALIZAMOS LAS TABLAS CORRESPONDIENTES A LAS PRUEBAS DE LABORATORIO
*/
--Table: locacion
INSERT INTO locacion (locacion_descrip, geom) VALUES ('Ceneha','{"type":"Point","coordinates":[-60.67147135734559,-31.639662926338005]}') */
--Table: nodo_red 
INSERT INTO nodo_red (fecha_desde,fecha_hasta,locacion_id,nod_id,rol_id,wsn_id) VALUES ('2017-04-01',null,1,1,1,1); -- Nodo_0 (Coordinador)
INSERT INTO nodo_red (fecha_desde,fecha_hasta,locacion_id,nod_id,rol_id,wsn_id) VALUES ('2017-04-01',null,1,2,2,1); -- Nodo_1 (Router)
INSERT INTO nodo_red (fecha_desde,fecha_hasta,locacion_id,nod_id,rol_id,wsn_id) VALUES ('2017-04-01',null,1,3,2,1); -- Nodo_2 (Router)
INSERT INTO nodo_red (fecha_desde,fecha_hasta,locacion_id,nod_id,rol_id,wsn_id) VALUES ('2017-04-01',null,1,4,3,1); -- Nodo_3 (Hoja)
INSERT INTO nodo_red (fecha_desde,fecha_hasta,locacion_id,nod_id,rol_id,wsn_id) VALUES ('2017-04-01',null,1,5,3,1); -- Nodo_4 (Hoja)
/*Estas tablas son completadas in situ mediante el Administrador Django.
--Table: dato;
--Table: configuracion_wsn;
*/
