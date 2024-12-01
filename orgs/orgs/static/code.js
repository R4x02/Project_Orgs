document.addEventListener('DOMContentLoaded', function() {
    const darkModeToggle = document.getElementById('dark-mode-toggle');
    const currentTheme = localStorage.getItem('theme');

    if (currentTheme === 'dark') {
        document.body.classList.add('dark-mode');
        darkModeToggle.textContent = 'Light Mode';
    }

    darkModeToggle.addEventListener('click', function() {
        document.body.classList.toggle('dark-mode');
        let theme = 'light';
        if (document.body.classList.contains('dark-mode')) {
            theme = 'dark';
            darkModeToggle.textContent = 'Light Mode';
        } else {
            darkModeToggle.textContent = 'Dark Mode';
        }
        localStorage.setItem('theme', theme);
    });

    const teamLinks = document.querySelectorAll('.team-name a');
    teamLinks.forEach(link => {
        link.addEventListener('mouseover', function() {
            const theme = localStorage.getItem('theme');
            if (theme === 'dark') {
                this.closest('.team-name a').style.backgroundColor = '#b36336';
                this.closest('.team-name a').style.color = '#fff';
            } else {
                this.closest('.team-name a').style.backgroundColor = '#d3d3d3';
                this.closest('.team-name a').style.color = '#000';
            }
        });
        link.addEventListener('mouseout', function() {
            this.closest('.team-name a').style.backgroundColor = '';
            this.closest('.team-name a').style.color = '';
        });
    });
});