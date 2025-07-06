// Client-side form validation
document.addEventListener('DOMContentLoaded', function() {
    // Add any client-side JS needed
    console.log('WhatsApp Reporter loaded');
    
    // Flash message auto-dismiss
    const flashMessages = document.querySelectorAll('.alert');
    flashMessages.forEach(msg => {
        setTimeout(() => {
            msg.style.transition = 'opacity 0.5s';
            msg.style.opacity = '0';
            setTimeout(() => msg.remove(), 500);
        }, 5000);
    });
});
