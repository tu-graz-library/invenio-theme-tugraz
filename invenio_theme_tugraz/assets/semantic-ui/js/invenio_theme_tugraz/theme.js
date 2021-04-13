import $ from 'jquery';
import 'semantic-ui-css';

let lastClickedElement = null;

// called on document ready
$(function() {

  // remove focus on click for outgoing links to reset css
  // store clicked element so tab index can be restored
  $('a').on('click', (eventHandler) => {
    let target = eventHandler.target;
    lastClickedElement = target;
    target.blur();
  })

  $(document).on('keydown', keyDownHandler);
  importZammadScript();
});

function importZammadScript() {
  let scriptNode = document.createElement("hidden"); //needed for zammad script
  scriptNode.id = "zammad_form_script";
  scriptNode.src = "https://ub-support.tugraz.at/assets/form/form.js";
  document.head.appendChild(scriptNode);
  
  $.getScript("https://ub-support.tugraz.at/assets/form/form.js", () => {
    $('#feedback-form').ZammadForm({
      messageTitle: 'Contact us',
      showTitle: true,
      messageSubmit: 'Submit',
      messageThankYou: 'Thank you for your message, (#%s). We will get back to you as quickly as possible!',
      modal: true
    });
  });
}

function keyDownHandler(keyDownEvent) {
  switch (keyDownEvent.key) {
    case 'Tab':
      // restore activeElement after clicking on outgoing link
      if (lastClickedElement !== null) {
        lastClickedElement.focus();
        lastClickedElement = null;
      }
      break;
    default:
      break;
  }
}


// used for sticky test instance notification
$('.ui.sticky.test-instance')
  .sticky({
    context: 'body'
  })
;

export function toggleVisibility(id) {
    var element = document.getElementById(id);
    var isHided = element.style.display === "none";

    element.style.display = isHided ? "block" : "none";
}

window.toggleVisibility = toggleVisibility;
