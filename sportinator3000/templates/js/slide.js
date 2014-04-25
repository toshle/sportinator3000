(function(){
Content = document.getElementsByTagName('main')[0];
Anchors = document.getElementsByTagName('nav')[0].getElementsByTagName('a');

for (var I = 0; I < Anchors.length; I++)
  Anchors[I].addEventListener('click', scroll, true);

function scroll(e)
{
  var url = (e.srcElement || e.target).href.
  replace(new RegExp('/(?=[a-z]*$)'), '/raw/');

  if (url)
    e.preventDefault();
  else
    return;

  var Request = new XMLHttpRequest();
  console.log(url);
}
})();
