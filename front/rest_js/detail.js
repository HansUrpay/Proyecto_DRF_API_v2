const html_title = document.querySelector("#html_title");
const html_prioridad = document.querySelector("#html_prioridad");
const html_created = document.querySelector("#html_created");
const html_usuario = document.querySelector("#html_usuario");

async function detailAPI() {
  try {
    const url = `http://127.0.0.1:8000/api2/${getID("id")}/`;
    const response = await fetch(url);
    // const data = await response.json();
    // Deconstruccion se basa en las key que posee
    const { title, prioridad, created_at, usuario } = await response.json();

    html_title.textContent = title;
    html_prioridad.textContent = prioridad;
    html_created.textContent = created_at;
    html_usuario.textContent = usuario;
  } catch (error) {
    console.log(error);
  }
}

function getID(pm_field) {
  const params = new URLSearchParams(window.location.search);
  return params.get(pm_field);
}

detailAPI();
