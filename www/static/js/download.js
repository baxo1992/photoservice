var url = "/www/download_list.html";

$.get(url, function (data) {
    $("#appendToThis").append(data);
});