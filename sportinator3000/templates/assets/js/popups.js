(function() {
  var register_link = document.getElementById("register_link");
  var register_field = document.getElementById("register_popup");
  var register_form = document.getElementById("register_form");

  register_field.addEventListener('click', register_onclick, false);
  register_link.addEventListener('click', register_onclick, false);
  register_form.addEventListener('click', noclose, false);

  function noclose(e) {
    if(!e) var e = window.event;
    e.cancelBubble = true;
    if(e.stopPropagation) e.stopPropagation();
  }

  function register_onclick(e) {
    e.preventDefault();
    register_popup();
  }

  function register_popup() {
    el = document.getElementById("register_popup");
    el.style.visibility = (el.style.visibility == "visible") ? "hidden" : "visible";
  }

  var forgotten_link = document.getElementById("forgotten_link");
  var forgotten_field = document.getElementById("forgotten_popup");
  var forgotten_form = document.getElementById("forgotten_form");

  forgotten_field.addEventListener('click', forgotten_onclick, false);
  forgotten_link.addEventListener('click', forgotten_onclick, false);
  forgotten_form.addEventListener('click', noclose, false);

  function forgotten_onclick(e) {
    e.preventDefault();
    forgotten_popup();
  }

  function forgotten_popup() {
    el = document.getElementById("forgotten_popup");
    el.style.visibility = (el.style.visibility == "visible") ? "hidden" : "visible";
  }
})();