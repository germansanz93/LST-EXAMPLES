const jwt = require('jsonwebtoken')
require('dotenv').config()
const secret = process.env.JWT_SECRET// Traemos el secreto desde .env.. En este caso estoy subiendo el .env al repo pero es algo que JAMAS deberia hacerse, es solo para que cuando descargues el repo tenga todo en orden
const users = require('./users.json');//Importamos los usuarios del json de users


module.exports = (req, res, next) => {
  const token = req.headers.authorization; //Extraemos el token desde el header
  try{
    console.log(token)
    const userEntity = jwt.verify(token, secret) //Extraemos la información contenida en el token. En este caso es toda la data del usuario.
    if(token && users.find(u => u.email == userEntity.email && u.password == u.password)){ //Validamos los valores que queramos del token
      console.log('Authorized')
      return next(); //Continuamos con el flujo normal de la llamada al endpoint
    }
  } catch {
    console.log("Error decrypting token. Token probably altered")
  }
  return res.status(401).send("Invalid Token, login again.")
}