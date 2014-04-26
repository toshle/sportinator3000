Map = {};

(function() {
  Map.Host = document.getElementsByTagName('article')[0];

  if (window.pos === undefined)
    window.pos = {
      lat: 42.687562,
      lng: 23.335213
    };

  Map.Position = new google.maps.LatLng(window.pos.lat, window.pos.lng);

  Map.SearchRadius = 1;

  Map.Options = {
      zoom: 16,
      center: Map.Position,
      disableDefaultUI: true
  };

  google.maps.event.addDomListener(window, 'load', LoadMap);

  function LoadMap() {
    Map.Map = new google.maps.Map(Map.Host, Map.Options);
    if (Map.DrawRadius !== undefined)
      Map.DrawRadius();
    else if (Map.PlaceAllMarkers !== undefined)
      Map.PlaceAllMarkers();
  }
})();
