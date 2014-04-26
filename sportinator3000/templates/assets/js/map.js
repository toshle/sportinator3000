(function() {
  var Host = document.getElementsByTagName('article')[0],
    Options = {
      zoom: 16,
      center: new google.maps.LatLng(42.68730, 23.33422),
      disableDefaultUI: true
    };

  google.maps.event.addDomListener(window, 'load', LoadMap);

  function LoadMap() {
    var Map = new google.maps.Map(Host, Options),

      Marker = new google.maps.Marker({
        position: new google.maps.LatLng(42.68730, 23.33422),
        map: Map,
        title: 'Hello World!'
      }),

      Info = new google.maps.InfoWindow({
        content: 'Test'
      });

    google.maps.event.addListener(Marker, 'click', function() {
      Info.open(Map, Marker);
    });
  }
})();
