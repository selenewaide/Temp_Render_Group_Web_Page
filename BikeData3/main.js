var animalContainer = document.getElementById("animal-info")
var btn = document.getElementById("btn");

btn.addEventListener("click", function() {
    var ourRequest = new XMLHttpRequest();
    ourRequest.open('GET', 'sample_bike_data.json');

    ourRequest.onload = function() {
        var ourData = JSON.parse(ourRequest.responseText);
        renderHTML(ourData);
    };

    ourRequest.send();
});

function renderHTML(data) {
    var htmlString = "";
    
    htmlString += "<table>";
    
    htmlString += "<tr>" + "<th>Number</th>" + 
        "<th>Name</th>" + 
        "<th>Banking</th>" + 
        "<th>Bonus</th>" + 
        "<th>Status</th>" + 
        "<th>Available Stands</th>" + 
        "<th>Available Bikes</th>" + 
        "<th>Latitude</th>" + 
        "<th>Longitude</th>" + 
        "</tr>";
    
    
    for (i = 0; i < data.length; i++) {
        htmlString += "<tr>" + "<td>" + data[i].number + "</td>" + 
            "<td>" + data[i].name + "</td>" +
            "<td>" + data[i].banking + "</td>" +
            "<td>" + data[i].bonus + "</td>" +
            "<td>" + data[i].status + "</td>" +
            "<td>" + data[i].available_bike_stands + "</td>" +
            "<td>" + data[i].available_bikes + "</td>" +
            "<td>" + data[i].position.lat + "</td>" +
            "<td>" + data[i].position.lng + "</td>" +
            "</tr>";
    }
    
    htmlString += "</table>";
    
    animalContainer.insertAdjacentHTML('beforeend', htmlString);
}