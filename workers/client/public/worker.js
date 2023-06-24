self.addEventListener("install", (event) => {
  //Agregamos los eventos de install y activate para disponer del worker inmediatamente
  event.waitUntil(self.skipWaiting());
  console.log("serviceworker installed!");
});

self.addEventListener("activate", (event) => {
  event.waitUntil(self.clients.claim());
  console.log("serviceworker ready!");
});

//Creamos un metodo para almacenar el token
self.addEventListener("message", (event) => {
  if (event.data && event.data.type == "SET_TOKEN") {
    token = event.data.token;
    console.log("token set!");
  }
  if (event.data && event.data.type == "CLEAR_TOKEN") {
    token = event.data.token;
    console.log("token cleared!");
  }
});

let token = "";

const privateRoutes = ["http://localhost:8080/private"];

//Funcion para agregar el token a las llamadas que sea necesario, para eso vamos a utilizar el evento de fetch
const addAuthHeader = function (event) {
  destURL = new URL(event.request.url);
  if (privateRoutes.includes(destURL.href)) {
    console.log(destURL.href);
    let modifiedHeaders = new Headers(event.request.headers);
    if (token) {
      modifiedHeaders.append("Authorization", token);
    }
    const authReq = new Request(event.request, {
      headers: modifiedHeaders,
      mode: "cors",
    });
    console.log("token added to request", authReq.headers, authReq.headers.get('Authorization'));
    for (const pair of modifiedHeaders.entries()) {
      console.log(`${pair[0]}: ${pair[1]}`);
    }
    event.respondWith((async () => fetch(authReq))());
  }
};

self.addEventListener('fetch', addAuthHeader); //Indicamos que al capturar un evento de tipo fetch se ejecute la funcion addAuthHeader
