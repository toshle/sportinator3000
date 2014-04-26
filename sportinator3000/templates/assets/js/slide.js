(function(){
  var Anchors = document.getElementsByTagName('nav')[0].getElementsByTagName('a');

  for (var I = 0; I < Anchors.length; I++)
    Anchors[I].addEventListener('click', scroll, true);

  function scroll(e)
  {
    var url = (e.srcElement || e.target).href,
      raw = url.replace(/\/(?=[a-z]*$)/, '/raw/') + '/';

    if (url)
      request(raw, e);
    else
      return;
  }

  function request(url, e)
  {
    var Request = new XMLHttpRequest();
    Request.open('GET', url);
    Request.send();

    Request.onreadystatechange = function()
    {
      if (Request.readyState === 4 && Request.status === 200)
      {
        e.preventDefault();
        update(Request.responseText, url);
      }

      else
        return;
    };
  }

  function update(text, url)
  {
      var Content = document.getElementsByTagName('main')[0];
      history.pushState({}, url, url);
      Content.innerHTML = text;
  }
})();
