document.addEventListener('DOMContentLoaded', function() {
    const btns = document.querySelectorAll('.funky-btn');

    btns.forEach(btn => {
        btn.addEventListener('mouseover', function() {
            this.classList.add('animate-pop');
        });

        btn.addEventListener('mouseout', function() {
            this.classList.remove('animate-pop');
        });
    });

    console.log("Funky HTTP Server JS Loaded.");
});
