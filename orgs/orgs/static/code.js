function darkliteFunc() {
    const body = document.body;
    body.classList.toggle('dark-mode');

    if (body.classList.contains('dark-mode')) {
        localStorage.setItem('theme', 'dark');
    } else {
        localStorage.setItem('theme', 'light');
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const theme = localStorage.getItem('theme');
    if (theme === 'dark') {
        document.body.classList.add('dark-mode');
    }
});


const teamLinks = document.querySelectorAll('.team-name a');

teamLinks.forEach(link => {
    link.addEventListener('mouseover', function() {
        const theme = localStorage.getItem('theme');
        if (theme === 'dark') {
            this.closest('.team-item button').style.backgroundColor = '#303030';
            this.closest('.team-name a').style.color = '#fff';
        } else {
            this.closest('.team-item button').style.backgroundColor = '#d3d3d3';
            this.closest('.team-name a').style.color = '#000';
        }
    });
    link.addEventListener('mouseout', function() {
        this.closest('.team-item button').style.backgroundColor = '';
        this.closest('.team-name a').style.color = '';
    });
});