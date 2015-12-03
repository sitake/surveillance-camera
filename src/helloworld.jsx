var React = require('react');
var ReactDOM = require('react-dom');

var Pict = React.createClass({
	render:function(){
		return(
			<img src={"static/image"+this.props.pict+".png?r="+Math.random()}/>
		);
	}
});

var HelloWorld = React.createClass({
	getInitialState:function(){
		return({pict:""});
	},
	componentDidMount:function(){
		var ws = new WebSocket("ws:"+window.location.host+"/test");
		ws.onopen = function(){
			ws.send("hello,world");
		};
		ws.onmessage = this.handleMessage
	},
	handleMessage:function(e){
		this.setState({pict:e.data});
	},
	render:function(){
		return(
			<div>
				<h1>研究室監視中！</h1>
				<Pict pict = {this.state.pict}/>
			</div>
		);
	}
});

ReactDOM.render(
	<HelloWorld />,
	document.getElementById('example')
);
