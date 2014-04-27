(function() {
  Map.DrawRadius = function() {
    var populationOptions = {
      strokeColor: '#FF0000',
      strokeOpacity: 0.8,
      strokeWeight: 2,
      fillColor: '#FF0000',
      fillOpacity: 0.15,
      map: Map.Map,
      center: Map.Position,
      radius: Map.Attrs.Radius * 1000
    };

    Map.Circle = new google.maps.Circle(populationOptions);
  };

  Map.FilteredDraw = function() {
    Map.DrawRadius();
    Map.PlaceMarkers('api/filtered?latitude=' + window.pos.lat +
      '&longitude=' + window.pos.lng + '&radius=10');
    Map.BindSearchControls();
  };

  Map.BindSearchControls = function() {
    document.getElementsByName('period')[0].onchange  = UpdateDuration;
    document.getElementsByName('sport')[0].onchange   = UpdateSport;
    document.getElementById('radius_slider').onchange = UpdateRadius;
    document.getElementById('price_slider').onchange  = UpdatePrice;
  };

  UpdateDuration = function() {
    Map.Attrs.Duration = this.value;
    Map.RedrawFiltered();
  };

  UpdateSport = function() {
    Map.Attrs.Sport = this.value;
    Map.RedrawFiltered();
  };

  UpdateRadius = function() {
    Map.Attrs.Radius = this.value;
    Map.RedrawFiltered();
  };

  UpdatePrice = function() {
    Map.Attrs.Price = this.value;
    Map.RedrawFiltered();
  };

  Map.RedrawFiltered = function() {
    Map.Circle.setMap(null);
    Map.RemoveAllMarkers();
    Map.DrawRadius();
    Map.PlaceFilteredMarkers();
  };

  Map.RemoveAllMarkers = function() {
    for (var Index in Map.Markers) {
      Map.Markers[Index].setMap(null);
  }};
})();
