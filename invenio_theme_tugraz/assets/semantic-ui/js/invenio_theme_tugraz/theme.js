export function hide() {
    var x = document.getElementById('heading');

    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}

window.hide = hide;
