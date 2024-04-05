document.addEventListener("DOMContentLoaded", function() {
    const headItems = document.querySelectorAll('.head');
    headItems.forEach(function(headItem) {
        headItem.addEventListener('click', function() {
            var index = this.getAttribute('data-index');
            var bodyItem = document.querySelector('.body[data-index="' + index + '"]');
            var currentDisplayStyle = bodyItem.style.display;
            if (currentDisplayStyle === '' || currentDisplayStyle === 'none') {
                bodyItem.style.display = 'block';
            } else {
                bodyItem.style.display = 'none';
            }
        });
    });
});