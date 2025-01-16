
function HeatingFloor() {
    // Get the checkbox
    var checkBox = document.getElementById("floorHeating");
  
    // If the checkbox is checked, display the output text
    if (checkBox.checked == true){
      // turn on the floor heating
      fetch('/turnOnFloorHeating')
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        console.log(data);
      })
      .catch(error => {
        console.error('Error:', error);
      });
      document.getElementById("burner").innerHTML = "Burner: ON";
      document.getElementById("floor").innerHTML = "Underfloor heating pump: ON";
    } else {
      // turn off the floor heating
      fetch('/turnOffFloorHeating')
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        console.log(data);
      })
      .catch(error => {
        console.error('Error:', error);
      });
      document.getElementById("burner").innerHTML = "Burner: OFF";
      document.getElementById("floor").innerHTML = "Underfloor heating pump: OFF";
    }
  }


function TowelRail() {
    // Get the checkbox
    var checkBox = document.getElementById("towelRail");
  
    // If the checkbox is checked, display the output text
    if (checkBox.checked == true){
      // turn on the towel rail
      fetch('/turnOnTowelRail')
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        console.log(data);
      })
      .catch(error => {
        console.error('Error:', error);
      });
      document.getElementById("burner").innerHTML = "Burner: ON";
      document.getElementById("rail").innerHTML = "Towel rail pump: ON";
    } else {
      // turn off the towel rail
      fetch('/turnOffTowelRail')
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        console.log(data);
      })
      .catch(error => {
        console.error('Error:', error);
      });
      document.getElementById("burner").innerHTML = "Burner: OFF";
      document.getElementById("rail").innerHTML = "Towel rail pump: OFF";
    }
  }

function updateState() {
    fetch('/getState')
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then(data => {
      console.log(data);
      if (data.floorHeating == 1) {
        document.getElementById("floorHeating").checked = true;
        document.getElementById("burner").innerHTML = "Burner: ON";
        document.getElementById("floor").innerHTML = "Underfloor heating pump: ON";
      } else {
        document.getElementById("floorHeating").checked = false;
        document.getElementById("burner").innerHTML = "Burner: OFF";
        document.getElementById("floor").innerHTML = "Underfloor heating pump: OFF";
      }
      if (data.towelRail == 1) {
        document.getElementById("towelRail").checked = true;
        document.getElementById("burner").innerHTML = "Burner: ON";
        document.getElementById("rail").innerHTML = "Towel rail pump: ON";
      } else {
        document.getElementById("towelRail").checked = false;
        document.getElementById("burner").innerHTML = "Burner: OFF";
        document.getElementById("rail").innerHTML = "Towel rail pump: OFF";
      }
    })
    .catch(error => {
      console.error('Error:', error);
    });
}