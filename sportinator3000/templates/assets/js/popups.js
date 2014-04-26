(function() {
  var register_link = document.getElementById("register_link");
  var register_field = document.getElementById("register_popup");
  var register_form = document.getElementById("register_form");

  register_field.addEventListener('click', onclick, false);
  register_link.addEventListener('click', onclick, false);
  register_form.addEventListener('click', noclose, false);

  function noclose(e) {
    if(!e) var e = window.event;
    e.cancelBubble = true;
    if(e.stopPropagation) e.stopPropagation();
  }

  function onclick(e) {
    e.preventDefault();
    register_popup();
  }

  function register_popup() {
    el = document.getElementById("register_popup");
    el.style.visibility = (el.style.visibility == "visible") ? "hidden" : "visible";
  }
})();