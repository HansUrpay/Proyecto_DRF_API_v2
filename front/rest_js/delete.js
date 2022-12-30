const html_title = document.querySelector("#html_title");
const html_delete = document.querySelector('#html_delete');

async function detailAPI() {
  try {
    const url = `http://127.0.0.1:8000/api2/${getID("id")}/`;
    const response = await fetch(url);
    // Deconstruccion se basa en las key que posee
    const { nombre } = await response.json();

    html_title.textContent = nombre;
  } catch (error) {
    console.log(error);
  }
}

function getID(pm_field) {
  const params = new URLSearchParams(window.location.search);
  return params.get(pm_field);
}

html_delete.onclick = async function () {
  console.log('conectado')
  const { isConfirmed, isDenied, isDismissed } = await Swal.fire({
    title: 'Do you want to save the changes?',
    showDenyButton: true,
    showCancelButton: true,
    confirmButtonText: 'Save',
    denyButtonText: `Don't save`,
  })

  if (isConfirmed) {
    try {
      const options = {
        method: "DELETE",
        headers: { "Content-Type": "application/json" }
      };
      const url = `http://127.0.0.1:8000/api2/${getID("id")}/`;
      const response = await fetch(url, options);

      location.href = '/rest_html/list.html'
  
      html_title.textContent = nombre;
    } catch (error) {
      console.log(error);
    }
  }
}

detailAPI();
