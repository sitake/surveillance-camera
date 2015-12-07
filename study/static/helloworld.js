var ws = new WebSocket("ws:"+window.location.host+"/socket");
ws.onopen = function(){
	ws.send("Hello, world!");
};
ws.onmessage = function(e){
	document.getElementById("example").textContent=e.data;
};

document.getElementById("example").textContent="Hello, world!";
