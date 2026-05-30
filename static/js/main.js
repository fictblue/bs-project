// Main JavaScript file for BS Website

document.addEventListener('DOMContentLoaded', function() {
    // Mobile menu toggle
    const mobileMenuButton = document.getElementById('mobile-menu-button');
    const mobileMenu = document.getElementById('mobile-menu');
    
    if (mobileMenuButton && mobileMenu) {
        mobileMenuButton.addEventListener('click', function() {
            mobileMenu.classList.toggle('hidden');
        });
    }
    
    // AI Chat functionality
    const chatForm = document.getElementById('chat-form');
    const chatInput = document.getElementById('chat-input');
    const chatMessages = document.getElementById('chat-messages');
    
    if (chatForm) {
        chatForm.addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const message = chatInput.value.trim();
            if (!message) return;
            
            // Add user message to chat
            addMessage(message, 'user');
            chatInput.value = '';
            
            try {
                const response = await fetch('/ai/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'X-CSRFToken': getCookie('csrftoken')
                    },
                    body: `message=${encodeURIComponent(message)}`
                });
                
                const data = await response.json();
                
                if (data.response) {
                    addMessage(data.response, 'ai');
                } else if (data.error) {
                    addMessage('Error: ' + data.error, 'error');
                }
            } catch (error) {
                addMessage('Error: ' + error.message, 'error');
            }
        });
    }
    
    function addMessage(text, type) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `mb-4 ${type === 'user' ? 'text-right' : 'text-left'}`;
        
        const bubble = document.createElement('div');
        bubble.className = `inline-block max-w-xs px-4 py-2 rounded-lg ${
            type === 'user' ? 'bg-purple-600 text-white' : 
            type === 'ai' ? 'bg-gray-200 text-gray-800' : 
            'bg-red-200 text-red-800'
        }`;
        bubble.textContent = text;
        
        messageDiv.appendChild(bubble);
        chatMessages.appendChild(messageDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
    
    function getCookie(name) {
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        if (parts.length === 2) return parts.pop().split(';').shift();
    }
});
