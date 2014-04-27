(function() {
  if (navigator.geolocation)
    navigator.geolocation.getCurrentPosition(SetGeoLocation);

  function SetGeoLocation(pos) {
    console.log(pos);
    if (pos.coords.latitude != 0)
      window.pos = {
        lat: pos.coords.latitude,
        lng: pos.coords.longitude
      };
  }
})();
