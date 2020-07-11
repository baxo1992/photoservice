jQuery(function($)
		{
			$.scrollTo(0);
			$('#link1').click(function(){ $.scrollTo($('#description1'), 500); });
			$('#link2').click(function(){ $.scrollTo($('#description2'), 500); });
			$('#link3').click(function(){ $.scrollTo($('#description3'), 500); });

		}
		);
		$(window).scroll(function()
		{
			if($(this).scrollTop()>300) $('.scrollup').fadeIn();
			else $('.scrollup').fadeOut();
		}

		);
