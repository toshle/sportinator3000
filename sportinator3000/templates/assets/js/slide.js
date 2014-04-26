(function() {
  var Anchors = document.getElementsByTagName('nav')[0].getElementsByTagName('a');

  for (var I = 0; I < Anchors.length; I++)
    Anchors[I].addEventListener('click', onclick, true);

  function onclick(e) {
    e.preventDefault();

    var abs = (e.srcElement || e.target).href,
      url = abs.replace(/^(?:\/\/|[^\/]+)*\//, ""),
      raw = 'raw/' + url + '/';
      base = abs.substr(0, abs.indexOf(url));

    if (url) {
      var Request = new XMLHttpRequest();
      Request.open('GET', base + raw);
      Request.send();

      Request.onreadystatechange = function() {
        if (Request.readyState == 4)
          update(Request.responseText, abs);
      };
    }
  }

  function update(text, url) {
    var Body = document.getElementsByTagName('body')[0],
      Old = document.getElementsByTagName('main')[0],
      New = document.createElement('main');

    New.innerHTML = text;
    New.className = 'new';
    Body.appendChild(New);
    Old.parentNode.removeChild(Old);
    New.className = '';
    history.replaceState({}, '', url);
  }
})();
