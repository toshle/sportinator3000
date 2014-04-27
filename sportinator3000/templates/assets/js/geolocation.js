var LoggedIn = document.getElementById('add') !== null;

(function() {
  if (location.href.indexOf('home') !== -1 ||
    location.href.indexOf('login') !== -1 ||
    location.href.indexOf('logout') !== -1)
      history.replaceState({}, '', '/');

  if (navigator.geolocation)
    navigator.geolocation.getCurrentPosition(SetGeoLocation);

  function SetGeoLocation(pos) {
    if (pos.coords.latitude != 0)
      window.pos = {
        lat: pos.coords.latitude,
        lng: pos.coords.longitude
      };
  }
})();
