//AQUI LLAMAMOS EXPRESS QUE ES UN FRAMEWORK DE NODE QUE PERMITE ESCRIBIR CODIGO DEL SERVIDOR DE MANERA SENCILLA.
//MORGAN, ES UN MODULO QUE PERMITE VER LAS PETICIONES POR CONSOLA.
//MODULOS PARA CREAR EL SERVIDOR: npm i express morgan
//MODULO PARA QUE EL SERVIDOR SE REINICIE EN MODO DESAROLLADOR: npm i nodemon -D

//LLAMAMOS LOS MODULOS
const express = require('express');
const app = express();
const morgan = require('morgan');

//CONFIGURACIONES, Proccess.env.PORT POR SI TENEMOS ALGUN SERVICIO EN LA NUBE COMO AZURE O HEROKU, ESTE TIENEN PUERTOS DEFINIDOS, 
//CON EN CASO EXISTE UN PUERTO DEFINIDO QUE LO TOME, SI NO QUE USE POR DEFECTO EL PUERTO 3000
app.set('port', process.env.PORT || 3000);

//MIDDELWARE
app.use(morgan('dev'));
app.use(express.urlencoded({extended: false}));
app.use(express.json());
 
//INICIAMOS EL SERVIDOR
app.listen(app.get('port'), () => {
    console.log(`Server on port ${app.get('port')}`);
}); 
