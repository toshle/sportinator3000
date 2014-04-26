Map.PlaceMarkers = function() {
  var Base = window.location.href.match(/^(?:\/\/|[^\/]+)*\//),
    Request = new XMLHttpRequest();

  Request.open('GET', Base + 'api/all');
  Request.send();

  Request.onreadystatechange = function() {
    if (Request.readyState == 4) {
      Map.MarkerObjects = JSON.parse(Request.responseText);
      placeMarkers();
    }
  };

  function placeMarkers() {
    Map.Markers = new Array(Map.MarkerObjects.length);
    for (var I = 0; I < Map.MarkerObjects.length; I++)
    {
      Mark = Map.MarkerObjects[I];

      Map.Markers[I] = new google.maps.Marker({
        position: new google.maps.LatLng(Mark.latitude, Mark.longitude),
        map: Map.Map,
        title: Mark.name
      });
    }
  }
};
