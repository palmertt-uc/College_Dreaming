function searchColleges() {
    searchTerm = document.getElementById("nav-search-bar");
    var getUrl = window.location;
    var baseUrl = getUrl .protocol + "//" + getUrl.host + "/"

    $.ajax({
        type: "GET",
        url: baseUrl + "api/search-universities/",
        data: {
            'query' : $('#nav-search-bar').val(),
        },
        success: searchSuccess,
    });
}

function searchSuccess(data, textStatus, jqXHR) {
    if(data.length == 0 || document.getElementById("nav-search-bar").value.length == 0) {
        document.getElementById("search-results").style.display = "none";
    }else {
        document.getElementById("search-results").style.display = "block";
    }

    document.getElementById("search-results-list").innerHTML = '';

    for(var i = 0; i < data.length; i++) {
        console.log(data[i]["instname"]);

        var listItem = document.createElement("LI");
        var listItemLink = document.createElement("a");
        var listItemCityState = document.createElement("span")
        var br = document.createElement("br");
                  
        // Create the text & link for anchor element. 
        var link = document.createTextNode(data[i]["instname"]); 
        listItemLink.appendChild(link);
        listItemLink.href = "/universities/" + data[i]["institutionid"];

        //Create the text for span element
        var cityState = document.createTextNode(data[i]["zipcodeid"]["cityid"]['city'] + ', ' + data[i]["zipcodeid"]["cityid"]['state']);
        listItemCityState.appendChild(cityState);

        listItem.appendChild(listItemLink);
        listItem.appendChild(listItemCityState);

        document.getElementById("search-results-list").appendChild(listItem);
    }
}

let searchResultList = document.getElementById('search-results');

document.addEventListener('click', function (e) {
    if (!searchResultList.contains(e.target)) {
        searchResultList.style.display = 'none';
    }
});