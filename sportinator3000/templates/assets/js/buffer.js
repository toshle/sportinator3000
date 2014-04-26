(function() {
  window.location.replace('/sports?latitude=' + window.pos.lat +
    '&longitude=' + window.pos.lng + '&radius' + Map.SearchRadius);
  history.replaceState({}, '', 'search');
}());
