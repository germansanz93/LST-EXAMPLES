const express = require('express'); //importamos express
const app = express(); //instanciamos express
const port = 8080; //definimos el puerto en el que vamos a servir el contenido
const jwt = require('jsonwebtoken')
const bodyParser = require("body-parser"); //Importamos body-parser
const users = require("./users.json");//Importamos los usuarios del json de users
const authMidleware = require('./authMidleware');
const cors = require('cors');
require('dotenv').config()

const secret = process.env.JWT_SECRET// Traemos el secreto desde .env.. En este caso estoy subiendo el .env al repo pero es algo que JAMAS deberia hacerse, es solo para que cuando descargues el repo tenga todo en orden

app.use(bodyParser.json()); //Configuramos body-parser, es necesario para poder interpretar el body de las peticiones
app.use(cors())

app.get('/', (req, res) => {
  //Definimos la ruta /
  res.send('Hello, World!');
});

app.post('/login', (req, res) => {
   //Ruta para hacer el login, valida que el usuario exista en db (simulado con el json en este caso)
  //y si user y pass coinciden, responde con el token de sesión.
  const { user, password } = req.body; //Hacemos destructuring y obtenemos el user y pass que nos envío el user
  console.log(user, password, req.body)
  const userEntity = users.find((u) => u.user_name === user);
  if (userEntity && password === userEntity.password) {
    //Si el user coincidió con el ingresado y la password también, procedemos a generar y responder el token
    //Por favor recorda que estamos trabajando con la password sin cifrar y que esto NUNCA debe hacerse. Solo lo hago asi para hacer mas corto el tutorial
    res.send({"token": jwt.sign(userEntity, secret, { expiresIn: 60 * 60 })})
  } else {
    res.status(401).send("Invalid credentials...");
  }
})

app.get('/private', authMidleware,(req, res, next) => { //Ruta que solo debemos mostrar a usuarios autenticados, agregamos el parametro next y llamamos al middleware
  res.send('Private')
})

app.use('*', (req, res) => { //Cualquier ruta que no hayamos definido respondera con este 404
  res.status(404).send('Are u lost?') //Importante que esta ruta sea la ultima, todas las rutas que definamos luego de esta no seran alcanzadas
})

app.listen(port, () => {
  //Le indicamos a express que debe escuchar por el puerto definido y logueamos para tener nocion de que estamos escuchando el puerto correcto
  console.log(`Listening on port ${port}`)
});