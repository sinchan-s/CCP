function getHitsValue() {
  var uiHits = document.getElementsByName("uiHits");
  for(var i in uiHits) {
    if(uiHits[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function getCHitsValue() {
  var uiCHits = document.getElementsByName("uiCHits");
  for(var i in uiCHits) {
    if(uiCHits[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function getMachineValue() {
  var uiMachine = document.getElementsByName("uiMachine");
  for(var i in uiMachine) {
    if(uiMachine[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function getRodValue() {
  var uiRod = document.getElementsByName("uiRod");
  for(var i in uiRod) {
    if(uiRod[i].checked) {
        return uiRod[i].value;
    }
  }
  return -1; // Invalid Value
}

function getMeshValue() {
  var uiMesh = document.getElementsByName("uiMesh");
  for(var i in uiMesh) {
    if(uiMesh[i].checked) {
        return uiMesh[i].value;
    }
  }
  return -1; // Invalid Value
}

function getPrintValue() {
  var uiPrint = document.getElementsByName("uiPrint");
  for(var i in uiPrint) {
    if(uiPrint[i].checked) {
        return uiPrint[i].value;
    }
  }
  return -1; // Invalid Value
}

function getFinishValue() {
  var uiFinish = document.getElementsByName("uiFinish");
  for(var i in uiFinish) {
    if(uiFinish[i].checked) {
        return uiFinish[i].value;
    }
  }
  return -1; // Invalid Value
}

function onClickedEstimateConsumption() {
  console.log("Estimate Consumption button clicked !!");
  var meter = document.getElementById("uiMeter");
  var cover = document.getElementById("uiCover");
  var speed = document.getElementById("uiSpeed");
  var viscosity = document.getElementById("uiViscosity");
  var hits = getHitsValue();
  var chits = getCHitsValue();
  var machine = getMachineValue();
  var rod = getRodValue();
  var mesh = getMeshValue();
  var print = getPrintValue();
  var finish = getFinishValue();
  var article = document.getElementById("uiArticle");
  var estConsum = document.getElementById("uiEstimatedConsumption");

  var url = "http://127.0.0.1:5000/predict_color_consum"; //Use this if you are NOT using nginx which is first 7 tutorials
  //var url = "/api/predict_color_consum"; // Use this if  you are using nginx. i.e tutorial 8 and onwards

  $.post(url, {  
    article: article.value,
    finish: finish,
    print: print,
    cover: cover,
    meters: meter,
    mesh: mesh,
    rod: rod,
    speed: speed,
    hits: hits,
    chits: chits,
    viscosity: viscosity,
    machine: machine
  },function(data, status) {
      console.log(data.estimated_consum);
      estConsum.innerHTML = "<h2>" + data.estimated_consum.toString() + " Kgs</h2>";
      console.log(status);
  });
}

function onPageLoad() {
  console.log( "document loaded" );
  var url = "http://127.0.0.1:5000/get_article_names"; // Use this if you are NOT using nginx which is first 7 tutorials
  //var url = "/api/get_article_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
  $.get(url,function(data, status) {
      console.log("got response for get_article_names request");
      if(data) {
          var article = data.article;
          var uiArticle = document.getElementById("uiArticle");
          $('#uiArticle').empty();
          for(var i in article) {
              var opt = new Option(article[i]);
              $('#uiArticle').append(opt);
          }
      }
  });
}

window.onload = onPageLoad;