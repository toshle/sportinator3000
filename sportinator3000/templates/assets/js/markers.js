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
    for (var Index in Objects) {
      var MarkerObj = Objects[Index];
      if (Map.Markers === undefined)
        Map.Markers = [];

      Marker = Map.Markers[Index] = new google.maps.Marker({
        position: new google.maps.LatLng(
              MarkerObj.latitude,
              MarkerObj.longitude
        ),
        map: Map.Map,
        title: MarkerObj.name,
      });

      Marker.Info = new google.maps.InfoWindow({
        content: '<a style="color: #357" href="details/' + MarkerObj.id + '">' +
          MarkerObj.description + '</a>'
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
  var Str = 'api/filters?latitude=' + Map.Position.k +
      '&longitude=' + Map.Position.A + '&radius=' + Map.Attrs.Radius;

  if (Map.Attrs.Sport != 0)
    Str += '&sport=' + Map.Attrs.Sport;

  if (Map.Attrs.Duration != 0)
    Str += '&duration=' + Map.Attrs.Duration;

  if (Map.Attrs.Price != 0)
    Str += '&price=' + Map.Attrs.Price;

  Map.PlaceMarkers(Str);
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
