var ws = new WebSocket("ws:"+window.location.host+"/test");
ws.onopen = function(){ws.send("hello,world!")};
ws.onmessage = function(e){
	document.getElementById('pict').src = "static/image0.png?r="+Math.random();
};

