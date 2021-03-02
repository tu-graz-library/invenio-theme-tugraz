import { jQuery, $ } from 'jquery';

$(function() {
  $('#feedback-form').ZammadForm({
    messageTitle: 'Feedback Form',
    messageSubmit: 'Send',
    messageThankYou: 'Thank you for your message, (#%s). We will get back to as quickly as possible!',
    modal: true
  });
});

export function toggleVisibility(id) {
    var element = document.getElementById(id);
    var isHided = element.style.display === "none";

    element.style.display = isHided ? "block" : "none";
}

window.toggleVisibility = toggleVisibility;
