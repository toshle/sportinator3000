Map = {};

// Dirty fix
function CloseModals() {
  Modals = document.getElementsByTagName('div');
  for (var Index in Modals) {
    if (!isNaN(Index) && Modals[Index] !== undefined && Modals[Index].className.indexOf('modal') !== -1) {
      Modals[Index].style.visibility = 'hidden';
      if (Map.NewMarker !== undefined)
        Map.RemoveAddMarker();
    }
  }
}

(function() {
  Map.Host = document.getElementsByTagName('article')[0];

  if (window.pos === undefined)
    window.pos = {
      lat: 42.674574,
      lng: 23.330401
      // lat: 42.687562,
      // lng: 23.335213
    };

  Map.Position = new google.maps.LatLng(window.pos.lat, window.pos.lng);
  Map.Attrs = {
    Radius: 10,
    Sport: 0,
    Duration: 0,
    Price: 200,
  };
  Map.Options = {
      zoom: 16,
      center: Map.Position,
      disableDoubleClickZoom: true,
      disableDefaultUI: true
  };

  google.maps.event.addDomListener(window, 'load', LoadMap);

  function LoadMap() {
    LoggedIn = document.getElementById('add') !== null;
    Map.Map = new google.maps.Map(Map.Host, Map.Options);
    if (Map.FilteredDraw !== undefined)
      Map.FilteredDraw();
    else if (Map.PlaceAllMarkers !== undefined)
      Map.PlaceAllMarkers();
  }
})();
