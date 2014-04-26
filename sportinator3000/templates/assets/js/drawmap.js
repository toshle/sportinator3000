Map = {};

(function() {
  Map.Host = document.getElementsByTagName('article')[0];

  if (window.Pos === undefined)
    window.Pos = {
      lat: 42.687562,
      len: 23.335213
    };

  Map.Options = {
      zoom: 16,
      center: new google.maps.LatLng(window.Pos.lat, window.Pos.lng),
      disableDefaultUI: true
  };

  google.maps.event.addDomListener(window, 'load', LoadMap);

  function LoadMap() {
    Map.Map = new google.maps.Map(Map.Host, Map.Options);
    if (Map.PlaceMarkers !== undefined)
      Map.PlaceMarkers();
  }
})();
