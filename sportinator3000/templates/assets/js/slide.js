(function() {
  var Anchors = document.getElementsByTagName('nav')[0].getElementsByTagName('a');

  for (var I = 0; I < Anchors.length; I++)
    Anchors[I].addEventListener('click', onclick, true);

  function onclick(e) {
    e.preventDefault();

    var abs = (e.srcElement || e.target).href,
      url = abs.replace(/^(?:\/\/|[^\/]+)*\//, ""),
      raw = 'raw/' + url;
    if (url) {
      var Request = new XMLHttpRequest();
      Request.open('GET', raw);
      Request.send();

      Request.onreadystatechange = function() {
        update(Request.responseText, url);
      };
    }
  }

  function update(text, url) {
    var Old = document.getElementsByTagName('main')[0],
      New = document.createElement('main');

    New.innerHTML = text;
    document.getElementsByTagName('body')[0].appendChild(New);

    Old.className = 'complete)old';
    Old.parentNode.removeChild(Old);
    history.pushState({}, url, url);
  }
})();
