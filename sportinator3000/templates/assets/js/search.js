(function() {
  Map.DrawRadius = function() {
    var populationOptions = {
      strokeColor: '#FF0000',
      strokeOpacity: 0.8,
      strokeWeight: 2,
      fillColor: '#FF0000',
      fillOpacity: 0.35,
      map: Map.Map,
      center: Map.Position,
      radius: Map.SearchRadius
    };

    Map.Circle = new google.maps.Circle(populationOptions);
  };
})();
