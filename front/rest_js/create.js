const html_forms = document.querySelector("form");
const inputs = document.querySelectorAll("input");
const select = document.querySelector("#usuario");

html_forms.onsubmit = async function (event) {
  event.preventDefault();

  const body = {
    usuario: select.value,
  };

  inputs.forEach((input) => {
    body[input.name] = input.value;
  });

  const body_json = JSON.stringify(body);
  try {
    const options = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: body_json,
    };

    const response = await fetch("http://127.0.0.1:8000/api2/", options);
    if (response.ok) {
      console.log("exito");
    } else {
      console.log("fallo");
    }
  } catch (error) {
    console.log("Algo pasó");
  }
};
