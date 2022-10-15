// Onclick of the button
document.querySelector("button").onclick = function () {
  // Call python's random_python function
  eel.get_list_of_all_files()(function(files){
    // Update the div with a random number returned by python
    document.getElementsByClassName("auswahl_datei").onclick = function () {
      for (const val of files) {
      var option = document.createElement("option");
      option.value = val;
      option.text = val;
      select.appendChild(option);
    }
      var label = document.createElement("label");
      label.innerHTML = "Datei auswählen";
      label.htmlFor = "vms";
      document.getElementsByClassName("auswahl_datei").appendChild(label).appendChild(select);
    }

    //document.querySelector(".auswahl_datei").innerHTML = files;
  })
}