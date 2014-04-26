Map.PlaceMarkers = function(url) {
  var Base = window.location.href.match(/^(?:\/\/|[^\/]+)*\//),
    Request = new XMLHttpRequest();

  Request.open('GET', Base + url);
  Request.send();

  Request.onreadystatechange = function() {
    if (Request.readyState == 4) {
      placeMarkers(JSON.parse(Request.responseText));
    }
  };

  function placeMarkers(Objects) {
    console.log(Objects);
    for (var Index in Objects) {
      var MarkerObj = Objects[Index];

      Marker = new google.maps.Marker({
        position: new google.maps.LatLng(
              MarkerObj.latitude,
              MarkerObj.longitude
        ),
        map: Map.Map,
        title: MarkerObj.name
      });

      Marker.Info = new google.maps.InfoWindow({
        content: MarkerObj.description
      });

      google.maps.event.addListener(Marker, 'click', Map.OpenInfo);
      google.maps.event.addListener(Map.Map, 'click', Map.AddMarker);
    }
  }
};

Map.PlaceAllMarkers = function() {
  Map.PlaceMarkers('api/all');
};

Map.PlaceFilteredMarkers = function() {
  Map.PlaceMarkers('api/filters?latitude=' + Map.Position.k +
      '&longitude=' + Map.Position.A + '&radius=' + Map.SearchRadius
      );
};

Map.OpenInfo = function() {
  this.Info.open(Map.Map, this);
  var Marker = this;
  setTimeout(function() {
    Marker.Info.close();
  }, 3000);
};

Map.AddMarker = function() {
  console.log(this);
  // this.Info.open(Map.Map, this);
};
