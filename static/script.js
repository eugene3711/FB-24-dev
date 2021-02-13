/*
let list_div = document.querySelector(".list")

let getGeo = () => {
    fetch("http://127.0.0.1:5000/geodata", { method: "GET" })
      .then(response => response.json())
      .then(responseText => {
        responseText.developments.forEach(element => {
          let listItem = document.createElement("li");
          listItem.innerText = element.name;
          listItem.setAttribute('id', element.id);
          listItem.classList.add("dev-item");       
          list_div.append(listItem);
        });
      }
      )}
getGeo
*/