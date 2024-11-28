document.addEventListener('DOMContentLoaded', function() {
    const teamLinks = document.querySelectorAll('.team-name a');

    teamLinks.forEach(link => {
        link.addEventListener('mouseover', function() {
            this.closest('.team-name').style.backgroundColor = 'lightblue';
        });

        link.addEventListener('mouseout', function() {
            this.closest('.team-name').style.backgroundColor = '';
        });
    });
});