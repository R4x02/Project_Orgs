document.addEventListener('DOMContentLoaded', () => {
    const chatForm = document.getElementById('chat-form');
    const chatBox = document.getElementById('chat-box');

    chatForm.addEventListener('submit', function (e) {
        e.preventDefault();
        const content = document.getElementById('message-content').value;

        fetch(chatForm.dataset.url, {
            method: "POST",
            headers: {
                "X-CSRFToken": chatForm.dataset.csrf,
                "Content-Type": "application/x-www-form-urlencoded"
            },
            body: `content=${encodeURIComponent(content)}`
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert(data.error);
            } else {
                const newMessage = document.createElement('p');
                newMessage.innerHTML = `<strong>${data.user}</strong>: ${data.content} <em>${data.timestamp}</em>`;
                chatBox.appendChild(newMessage);
                document.getElementById('message-content').value = '';
            }
        });
    });
});
