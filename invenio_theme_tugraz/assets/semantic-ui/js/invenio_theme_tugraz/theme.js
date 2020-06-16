export function toggleVisibility(id) {
    var element = document.getElementById(id);
    var isHided = element.style.display === "none";

    element.style.display = isHided ? "block" : "none";
}

window.toggleVisibility = toggleVisibility;
