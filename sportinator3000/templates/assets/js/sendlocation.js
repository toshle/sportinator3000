(function() {
  var Host = document.getElementsByTagName('article')[0],
    Options = {
      zoom: 16,
      center: new google.maps.LatLng(42.68730, 23.33422),
      disableDefaultUI: true
    },
    Location = {},
    Position = {},
    Markers = [],
    Info = {},
    Map = {};

  google.maps.event.addDomListener(window, 'load', LoadMap);

  function LoadMap() {
    GeoLocation();

    Map = new google.maps.Map(Host, Options),

    Position = new google.maps.LatLng(Location.lat, Location.lng);

    Markers[0] = new google.maps.Marker({
      position: new google.maps.LatLng(42.68730, 23.33422),
      map: Map,
      title: 'Welcome'
    }),

    Info = new google.maps.InfoWindow({
      content: 'Test'
    });
}

  function GeoLocation() {
    navigator.geolocation.getCurrentPosition(SetLocation);
  }

  function SetLocation(Pos) {
    Position = new google.maps.LatLng(Pos.coords.latitude, Pos.coords.longitude);

    google.maps.event.addListener(Markers[0], 'click', function() {
      Markers[1] = new google.maps.Marker({
        position: Position,
        map: Map,
        title: ''
      });
      Info.open(Map, Markers[1]);
      Map.panTo(Position);
    });
  }
})();
