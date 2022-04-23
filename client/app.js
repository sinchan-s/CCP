function getRodValue() {
  var uiRod = document.getElementsByName("uiRod");
  for(var i in uiRod) {
    if(uiRod[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function getMeshValue() {
  var uiMesh = document.getElementsByName("uiMesh");
  for(var i in uiMesh) {
    if(uiMesh[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function getPrintValue() {
  var uiMesh = document.getElementsByName("uiPrint");
  for(var i in uiPrint) {
    if(uiPrint[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function onClickedEstimateColor() {
  console.log("Estimate Consumption button clicked !!");
  var meter = document.getElementById("uiMeter");
  var cover = document.getElementById("uiCover");
  var speed = document.getElementById("uiSpeed");
  var rod = getRodValue();
  var mesh = getMeshValue();
  var print = getPrintValue();
  var article = document.getElementById("uiArticle");
  var estConsum = document.getElementById("uiEstimatedConsumption");

  //var url = "http://127.0.0.1:5000/predict_home_price"; //Use this if you are NOT using nginx which is first 7 tutorials
  var url = "/api/predict_home_price"; // Use this if  you are using nginx. i.e tutorial 8 and onwards

  $.post(url, {
      meters: meter,
      cover: cover,
      speed: speed,
      rod: rod,
      mesh: mesh,
      print: print,
      article: article.value
  },function(data, status) {
      console.log(data.estimated_price);
      estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " Lakh</h2>";
      console.log(status);
  });
}

function onPageLoad() {
  console.log( "document loaded" );
  //var url = "http://127.0.0.1:5000/get_location_names"; // Use this if you are NOT using nginx which is first 7 tutorials
  var url = "/api/get_location_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
  $.get(url,function(data, status) {
      console.log("got response for get_location_names request");
      if(data) {
          var locations = data.locations;
          var uiLocations = document.getElementById("uiLocations");
          $('#uiLocations').empty();
          for(var i in locations) {
              var opt = new Option(locations[i]);
              $('#uiLocations').append(opt);
          }
      }
  });
}

window.onload = onPageLoad;