(function() {
  var Base = window.location.href.match(/^(?:\/\/|[^\/]+)*\//),
    Request = new XMLHttpRequest();

  Request.open('GET', Base + 'api');
  Request.send();

  Request.onreadystatechange = function() {
    if (Request.readyState == 4)
      console.log(Request.responseText);
  };
})();
