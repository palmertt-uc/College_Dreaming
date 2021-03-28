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

function largeSearchColleges() {
    searchTerm = document.getElementById("search-input");
    let getUrl = window.location;
    let baseUrl = getUrl .protocol + "//" + getUrl.host + "/"

    $.ajax({
        type: "GET",
        url: baseUrl + "api/search-universities/",
        data: {
            'query' : $('#search-input').val(),
        },
        success: largeSearchSuccess,
    });
}

function largeSearchSuccess(data, textStatus, jqXHR) {
    if(data.length === 0 || document.getElementById("search-input").value.length === 0) {
        document.getElementById("large-search-results").style.display = "none";
    }else {
        document.getElementById("large-search-results").style.display = "block";
    }

    document.getElementById("large-search-results-list").innerHTML = '';

    for(let i = 0; i < data.length; i++) {
        console.log(data[i]["instname"]);

        let listItem = document.createElement("LI");
        let listItemLink = document.createElement("a");
        let listItemCityState = document.createElement("span")
        let br = document.createElement("br");

        // Create the text & link for anchor element.
        let link = document.createTextNode(data[i]["instname"]);
        listItemLink.appendChild(link);
        listItemLink.href = "/universities/" + data[i]["institutionid"];

        //Create the text for span element
        let cityState = document.createTextNode(data[i]["zipcodeid"]["cityid"]['city'] + ', ' + data[i]["zipcodeid"]["cityid"]['state']);
        listItemCityState.appendChild(cityState);

        listItem.appendChild(listItemLink);
        listItem.appendChild(listItemCityState);

        document.getElementById("large-search-results-list").appendChild(listItem);
    }
}

let searchResultList = document.getElementById('search-results');
let searchPopup = document.querySelector('.search-popup');
let brandName = document.querySelector('.brand-name');

document.addEventListener('click', function (e) {
    let largeSearchResultList = $('#large-search-results');

    if (!largeSearchResultList.is(e.target) && largeSearchResultList.has(e.target).length === 0) {
        largeSearchResultList.hide();
    }

    if (!searchResultList.contains(e.target)) {
        searchResultList.style.display = 'none';
    }
});

function openSearchForm() {
    if (searchPopup.style.display === 'block') {
        searchPopup.style.display = 'none';
        brandName.style.visibility = 'visible';
    } else {
        searchPopup.style.display = 'block';
        brandName.style.visibility = 'hidden';
    }
}