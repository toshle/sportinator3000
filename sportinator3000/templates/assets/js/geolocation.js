(function() {
  if (navigator.geolocation)
    navigator.geolocation.getCurrentPosition(SetGeoLocation);

  function SetGeoLocation(Pos) {
    if (Pos.coords.latitude !== 0)
      window.Pos = {
        lat: Pos.coords.latitude,
        lng: Pos.coords.longitude
      };
  }
})();
