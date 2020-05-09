$(window).resize(function(){
	// alert("EARA");
	mapwidth=$(".m-portlet__head").width(),mapheight=$(".m-portlet__head").height();

	piewidth = ($(".m-portlet__head").width()/2.3)
	drawRegionsMap();
	pie();
})
