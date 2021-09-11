(function() {

    const langs = document.querySelector('.languages');
    const langs_dropdown = document.getElementById('langs-dropdown');
    langs.style.visibility  = 'hidden';

    langs_dropdown.addEventListener('click', function() {
        if(langs.style.visibility  === 'hidden') {
            langs.style.height = '10px';
            langs.style.visibility  = 'visible';
            const interval = window.setInterval(function() {
                if(numberize(langs) < 150)
                    return pixelize(langs);
                window.clearInterval(interval);
            }, 10);
            return;
        }
        const interval = window.setInterval(function() {
            if(numberize(langs) > 0)
                return pixelize(langs, -10);
            langs.style.visibility = 'hidden';
            window.clearInterval(interval);
        }, 10);
    });

    function numberize(el) {
        return Number(el.style.height.replace('px', ''));
    }

    function pixelize(el, add) {
        add = add || 10;
        el.style.height = numberize(el) + add + 'px';
    }

})();