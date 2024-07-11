document.addEventListener("DOMContentLoaded", function () {
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

    const nameSearch = document.getElementById('name-search');
    const tags = document.querySelectorAll('.tag');
    const projects = document.querySelectorAll('.project');

    function filterProjects() {
        const nameQuery = nameSearch.value.toLowerCase();

        projects.forEach((project) => {
            const name = project.getAttribute('data-name').toLowerCase();
            const nameMatch = name.includes(nameQuery);

            if (nameMatch) {
                project.style.display = "";
            } else {
                project.style.display = "none";
            }
        });
    }

    let selectedTags = [];

    tags.forEach((tag) => {
        tag.addEventListener("click", function () {
            const selectedTag = this.getAttribute('data-tag');

            if (selectedTags.includes(selectedTag)) {
                selectedTags = selectedTags.filter(tag => tag !== selectedTag);
                this.classList.remove('selected-tag');
            } else {
                selectedTags.push(selectedTag);
                this.classList.add('selected-tag');
            }

            projects.forEach((project) => {
                const projectTags = project.getAttribute('data-tags').split(', ');
                const hasMatchingTag = selectedTags.length === 0 || selectedTags.some(tag => projectTags.includes(tag));

                if (hasMatchingTag) {
                    project.style.display = "";
                } else {
                    project.style.display = "none";
                }
            });
        });
    });

    nameSearch.addEventListener("keyup", filterProjects);
});
