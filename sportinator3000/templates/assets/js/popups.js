(function() {

  function noclose(e) {
    if(!e) e = window.event;
    e.cancelBubble = true;
    if(e.stopPropagation) e.stopPropagation();
  }

  var add_activity_link  = document.getElementById("add_activity_link");
  var add_activity_field = document.getElementById("add_activity_popup");
  var add_activity_form  = document.getElementById("add_activity_form");

  if (add_activity_field != undefined || add_activity_field != null) {
    add_activity_field.addEventListener('click', add_activity_onclick, false);
    add_activity_link.addEventListener('click', add_activity_onclick, false);
    add_activity_form.addEventListener('click', noclose, false);
  }

  function add_activity_onclick(e) {
    e.preventDefault();
    add_activity_popup();
  }

  function add_activity_popup() {
    var el = document.getElementById("add_activity_popup");
    el.style.visibility = (el.style.visibility == "visible") ? "hidden" : "visible";
  }

  var register_link  = document.getElementById("register_link");
  var register_field = document.getElementById("register_popup");
  var register_form  = document.getElementById("register_form");

  if (register_field != undefined || register_field != null) {
    register_field.addEventListener('click', register_onclick, false);
    register_link.addEventListener('click', register_onclick, false);
    register_form.addEventListener('click', noclose, false);
  }

  function register_onclick(e) {
    e.preventDefault();
    register_popup();
  }

  function register_popup() {
    var el = document.getElementById("register_popup");
    el.style.visibility = (el.style.visibility == "visible") ? "hidden" : "visible";
  }

  var forgotten_link  = document.getElementById("forgotten_link");
  var forgotten_field = document.getElementById("forgotten_popup");
  var forgotten_form  = document.getElementById("forgotten_form");

  if (forgotten_field != undefined || forgotten_field != null) {
    forgotten_field.addEventListener('click', forgotten_onclick, false);
    forgotten_link.addEventListener('click', forgotten_onclick, false);
    forgotten_form.addEventListener('click', noclose, false);
  }

  function forgotten_onclick(e) {
    e.preventDefault();
    forgotten_popup();
  }

  function forgotten_popup() {
    var el = document.getElementById("forgotten_popup");
    el.style.visibility = (el.style.visibility == "visible") ? "hidden" : "visible";
  }

})();
