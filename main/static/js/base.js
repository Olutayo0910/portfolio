document.getElementById('menu-button').addEventListener('click', function() {
    var menu = document.getElementById('menu');
    var menuIcon = document.getElementById('menu-icon');
    var menuPath = document.getElementById('menu-path');

    if (menu.classList.contains('hidden-nav')) {
        menu.classList.remove('hidden-nav');
        menu.classList.add('visible-nav');
        menuPath.setAttribute('d', 'M6 18L18 6M6 6l12 12');
    } else {
        menu.classList.remove('visible-nav');
        menu.classList.add('hidden-nav');
        menuPath.setAttribute('d', 'M4 6h16M4 12h16m-7 6h7');
    }
});