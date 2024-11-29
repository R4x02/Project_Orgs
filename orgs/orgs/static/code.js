document.addEventListener('DOMContentLoaded', function() {
    const teamLinks = document.querySelectorAll('.team-name a');

    teamLinks.forEach(link => {
        link.addEventListener('mouseover', function() {
            this.closest('.team-item').style.backgroundColor = '#f5f5f5';
        });

        link.addEventListener('mouseout', function() {
            this.closest('.team-item').style.backgroundColor = '';
        });
    });
});

function darkliteFunc() {
    document.querySelectorAll('*:not(item-name)').forEach(element => {
        element.classList.toggle('dark-mode');
    });

    if (document.querySelector('body').classList.contains('dark-mode')) {
        localStorage.setItem('darkMode', 'enabled');
    } else {
        localStorage.removeItem('darkMode');
    }
}