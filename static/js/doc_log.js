(function($) {
    "use strict";
    /* ..............................................
	Loader 
    ................................................. */
	
	$(window).on('load', function() { 
		$('.preloader').fadeOut(); 
		$('#preloader').delay(1000).fadeOut('slow'); 
		$('body').delay(1500).css({'overflow':'visible'});
    });
    
}(jQuery));