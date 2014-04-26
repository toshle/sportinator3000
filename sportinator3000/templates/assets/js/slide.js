(function() {
  var Anchors = document.getElementsByTagName('nav')[0].getElementsByTagName('a');

  for (var I = 0; I < Anchors.length; I++)
    Anchors[I].addEventListener('click', onclick, true);

  function onclick(e) {
    e.preventDefault();

    var url = (e.srcElement || e.target).href,
      raw = url.replace(/\/(?=[a-z]*$)/, '/raw/') + '/';

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

    Old.className = 'old';
    Old.parentNode.removeChild(Old);
    history.pushState({}, url, url);
  }
})();
