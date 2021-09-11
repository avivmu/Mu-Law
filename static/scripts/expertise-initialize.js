(function() {

    var vm = {
        active: ko.observable(null),
        activate: function(index) {
            console.log('hii!')
            if(this.active() === index) {
                return this.active(null);
            }
            this.active(index);
        }
    }

    ko.applyBindings(vm, document.querySelector('.expertise-menu'));
})();