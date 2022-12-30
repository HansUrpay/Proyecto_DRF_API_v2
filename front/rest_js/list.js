const html_botones = document.querySelector("#botones");
const html_list = document.querySelector("#html_list");

const url = "http://127.0.0.1:8000/api2/";

async function getAPI() {
  try {
    const options = {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        'Authorization': 'Bearer ' + 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjcyMjc3MDc4LCJpYXQiOjE2NzIxOTA2NzgsImp0aSI6ImQ1M2NiZDdhYTQxYzRjNTQ4OGIzZmRhMmE0MDQwYTg5IiwidXNlcl9pZCI6MX0.GApOXkngqEW1-5Fj4EW_4GIoQIPAmPYAqh4Qlq3sEBQ'
      }
    };
console.log(options)
    const response = await fetch(url, options);
    const data = await response.json();
    data.forEach((value) => {
      html_list.innerHTML += listar_data(value);
    });
  } catch (error) {
    console.log(error);
  }
}

function listar_data(value) {
  return `
  <li>Nombre: <strong>${value.nombre}</strong></li>
  <li>Prioridad: ${value.prioridad}</li>
  <li>Creacion: ${value.created_at}</li>
  <a href="/rest_html/detail.html?hola=1&id=${value.id}">Detalles</a>
  <a href="/rest_html/delete.html?hola=1&id=${value.id}">Delete</a>
  <a href="/rest_html/update.html?hola=1&id=${value.id}">Update</a>
  <hr></hr>
  `;
}

getAPI();
