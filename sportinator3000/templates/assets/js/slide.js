(function(){
var Anchors = document.getElementsByTagName('nav')[0].getElementsByTagName('a');

for (var I = 0; I < Anchors.length; I++)
  Anchors[I].addEventListener('click', scroll, true);

function scroll(e)
{
  var url = (e.srcElement || e.target).href.
  replace(new RegExp('/(?=[a-z]*$)'), '/raw/') + '/';

  if (url)
  {
    var newView = request(url);
    console.log(newView);
    if (newView === '')
      return;
    else
      e.preventDefault();
      update(newView);
  }
  else
    return;
  }

function request(url)
{
var Request = new XMLHttpRequest();
  Request.open('GET', url);
  Request.send();

  Request.onreadystatechange = function()
  {
    if (Request.readyState === 4 && Request.status === 200)
      return Request.responseText;
    else
      return '';
  };
}})();

function update(text)
{
  var Content = document.getElementsByTagName('main')[0];
  Content.innerHTML = text;
}
