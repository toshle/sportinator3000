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
      google.maps.event.addListener(Map.Map, 'dblclick', Map.AddMarker);
      if (Map.Circle)
        google.maps.event.addListener(Map.Circle, 'dblclick', Map.AddMarker);
      google.maps.event.addListener(Map.Map, 'rclick', Map.AddMarker);
    }
  }
};

Map.PlaceAllMarkers = function() {
  Map.PlaceMarkers('api/all');
};

Map.PlaceFilteredMarkers = function() {
  var Str = 'api/filters?latitude=' + Map.Position.k +
      '&longitude=' + Map.Position.A + '&radius=' +
      Map.Attrs.Radius + '&price=' + Map.Attrs.Price;

  if (Map.Attrs.Sport != 0)
    Str += '&sport=' + Map.Attrs.Sport;

  if (Map.Attrs.Duration != 0)
    Str += '&duration=' + Map.Attrs.Duration;

  Map.PlaceMarkers(Str);
};

Map.OpenInfo = function() {
  this.Info.open(Map.Map, this);
  var Marker = this;
  setTimeout(function() {
    Marker.Info.close();
  }, 3000);
};

Map.AddMarker = function(e) {
  if (Map.NewMarker === undefined) {
    Map.NewMarker = new google.maps.Marker({
      position: e.latLng,
      map: Map.Map,
      title: 'New Marker',
      icon: '/assets/img/flag.png'
    });

    Orig = document.getElementById('add');
    date = new Date();
    dateStr = date.getYear() + '-' + date.getMonth() + '-' + date.getDay() +
      ' ' + date.getHours() + ':' + date.getMinutes();
    console.log(dateStr);

    Map.NewMarker.Modal = document.createElement('div');
    Map.NewMarker.Modal.className = 'modal';
    Map.NewMarker.Modal.innerHTML = Orig.innerHTML;
    document.body.appendChild(Map.NewMarker.Modal);
    document.getElementsByName('latitude')[0].value = e.latLng.k;
    document.getElementsByName('longitude')[0].value = e.latLng.A;
    document.getElementsByName('date_added')[0].value = dateStr;

    Map.NewMarker.Modal.style.visibility = 'visible';
  }
};

Map.RemoveAddMarker = function() {
  document.body.removeChild(Map.NewMarker.Modal);
  Map.NewMarker.setMap(null);
  Map.NewMarker = undefined;
}
