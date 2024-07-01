document.addEventListener("DOMContentLoaded", function () {
    // Select the input element where the user will type their search query
    const nameSearch = document.getElementById('name-search');
    
    // Select all elements with the class 'tag' (tags buttons)
    const tags = document.querySelectorAll('.tag');
    
    // Select all elements with the class 'projects' (individual project elements)
    const projects = document.querySelectorAll('.projects');

    /**
     * Filters the projects based on the user's search query.
     * It compares the data-name attribute of each project with the search query.
     * If the project's name includes the search query, it remains visible.
     * Otherwise, it is hidden.
     */
    function filterProjects() {
        // Get the current value of the search input, converted to lowercase
        const nameQuery = nameSearch.value.toLowerCase();
        
        console.log('Filtering projects with query:', nameQuery); // Debugging log

        // Iterate over each project element
        projects.forEach((project) => {
            // Get the value of the data-name attribute of the project, converted to lowercase
            const name = project.getAttribute('data-name').toLowerCase();
            
            console.log('Project name:', name); // Debugging log
            
            // Check if the project's name includes the search query
            const nameMatch = name.includes(nameQuery);
            
            console.log('Name match:', nameMatch); // Debugging log

            // Show the project if there's a match, otherwise hide it
            if (nameMatch) {
                project.style.display = "";
            } else {
                project.style.display = "none";
            }
        })
    }
    // Array to keep track of the currently selected tags
    let selectedTags = [];
    let currentSelectedTag = null;
    tags.forEach((tag) => {
        // when you click on each tag
        tag.addEventListener("click", function () {

            // select a tag from the tag list
            const selectedTag = this.getAttribute('data-tag');

            if (selectedTags.includes(selectedTag)) {
                // If selected, remove it from the selectedTags array and remove the 'selected-tag' class
                selectedTags = selectedTags.filter(tag => tag !== selectedTag);
                this.classList.remove('selected-tag');
            } else {
                // If not selected, add it to the selectedTags array and add the 'selected-tag' class
                selectedTags.push(selectedTag);
                this.classList.add('selected-tag');
            }

            // for each project
            projects.forEach((project) => {
                // select tags from each project's tag list
                const projectTags = project.getAttribute('data-tags').split(', ');

                // Check if any of the selected tags are in the project's tags
            const hasMatchingTag = selectedTags.length === 0 || selectedTags.some(tag => projectTags.includes(tag));

                // if the selected tag is present in a project tag list, leave the project visible
                // otherwise, hide the project
                if (hasMatchingTag) {
                    project.style.display = "";
                } else {
                    project.style.display = "none";
                }
            });
        });
    });

    // Attach an event listener to the search input to call filterProjects() on keyup
    nameSearch.addEventListener("keyup", filterProjects);
});
