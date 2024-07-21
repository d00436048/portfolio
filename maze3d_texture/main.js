import { initShaderProgram } from "./shader.js";
import { drawCircle, drawRectangle, drawTriangle, drawLineStrip } from "./shapes2d.js";
import { randomDouble } from "./random.js";
import { Maze} from "./maze.js";
import { Rat } from "./rat.js";
import {TOP_VIEW, OBSERVATION_VIEW, RATS_VIEW} from "./constants.js";

main();
async function main() {
	console.log('This is working');

	//
	// start gl
	// 
	const canvas = document.getElementById('glcanvas');
	const gl = canvas.getContext('webgl');
	if (!gl) {
		alert('Your browser does not support WebGL');
	}
	gl.clearColor(0.75, 0.85, 0.8, 1.0);
	gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);
	gl.enable(gl.DEPTH_TEST);
	gl.depthFunc(gl.LEQUAL);

	//
	// Create shaders
	// 
	const shaderProgram = initShaderProgram(gl, await (await fetch("uvTriangles.vs")).text(), await (await fetch("uvTriangles.fs")).text());

	// Load a texture and move it to the gpu
	gl.activeTexture(gl.TEXTURE0);
	gl.bindTexture(gl.TEXTURE_2D, loadTexture(gl, 'sandra512.jpg'));
	gl.uniform1i(gl.getUniformLocation(shaderProgram, "uTexture0"), 0);

	gl.activeTexture(gl.TEXTURE3);// Do we need this?

	//
	// Create content to display
	//
	const WIDTH = 5;
	const HEIGHT = 5;
	const m = new Maze(WIDTH, HEIGHT);
	const r = new Rat(.5, .5, 90, m);

	let currentView = OBSERVATION_VIEW;

	//
	// load a projection matrix onto the shader
	// 
	const margin = 0.5;
	let xlow = 0.0-margin;
	let xhigh = WIDTH+margin;
	let ylow = 0.0-margin;
	let yhigh = HEIGHT+margin;
	// squareWorld();

	// window.addEventListener('resize', squareWorld);
	// 3d code




	//
	// load a modelview matrix onto the shader
	// 
	const modelViewMatrixUniformLocation = gl.getUniformLocation(shaderProgram, "uModelViewMatrix");
	const identityMatrix = mat4.create();
    gl.uniformMatrix4fv(modelViewMatrixUniformLocation, false, identityMatrix);

	//
	// Register Listeners
	//
	addEventListener("click", click);
	function click(event) {
		console.log("click");
		const xWorld = xlow + event.offsetX / gl.canvas.clientWidth * (xhigh - xlow);
		const yWorld = ylow + (gl.canvas.clientHeight - event.offsetY) / gl.canvas.clientHeight * (yhigh - ylow);
		// Do whatever you want here, in World Coordinates.
	}

	let spinLeft = false;
	let spinRight = false;
	let scurryForward = false;
	let scurryBackward = false;
	let strafeLeft = false;
	let strafeRight = false;
	let goFast = false;

	window.addEventListener("keydown", keyDown);
	function keyDown(event){
		if (event.code == 'KeyQ'){
			spinLeft = true;
		}		
		if (event.code == 'KeyW'){
			scurryForward = true;
		}
		if (event.code == 'KeyA'){
			strafeLeft = true;
		}
		if (event.code == 'KeyE'){
			spinRight = true;
		}
		if (event.code == 'KeyS'){
			scurryBackward = true;
		}
		if (event.code == 'KeyD'){
			strafeRight = true;
		}
		if (event.code == 'KeyO'){
			currentView = OBSERVATION_VIEW;
		}
		if (event.code == 'KeyT'){
			currentView = TOP_VIEW;
		}
		if (event.code == 'KeyR'){
			currentView = RATS_VIEW;
		}
		if(event.code == 'KeyF'){
			goFast=true;
		}
	}
	window.addEventListener("keyup", keyUp);
	function keyUp(event){
		if (event.code == 'KeyQ'){
			spinLeft = false;
		}
		if (event.code == 'KeyW'){
			scurryForward = false;
		}
		if (event.code == 'KeyA'){
			strafeLeft = false;
		}
		if (event.code == 'KeyE'){
			spinRight = false;
		}
		if (event.code == 'KeyS'){
			scurryBackward = false;
		}
		if (event.code == 'KeyD'){
			strafeRight = false;
		}
		if(event.code == 'KeyF'){
			goFast=false;
		}
	}

	//
	// Main render loop
	//
	let previousTime = 0;
	function redraw(currentTime){
		currentTime *= .001; // milliseconds to seconds
		let DT = currentTime - previousTime;
		if(DT > .1)
			DT = .1;
		previousTime = currentTime;

		gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);

		if(spinLeft){
			r.spinLeft(DT);
		}
		if(scurryForward){
			r.scurryForward(DT);
		}
		if(strafeLeft){
			r.strafeLeft(DT);
		}
		if(spinRight){
			r.spinRight(DT);
		}
		if(scurryBackward){
			r.scurryBackward(DT);
		}
		if(strafeRight){
			r.strafeRight(DT);
		}
		if(goFast){
			r.scurryForward(DT*2);
		}
		//choose correct projection matrix
		if(currentView == OBSERVATION_VIEW){
			setObserveView(gl, shaderProgram,WIDTH,HEIGHT,canvas);
		}
		else if(currentView == TOP_VIEW){
			setTopView(gl, shaderProgram,WIDTH,HEIGHT,canvas);
		}
		else if(currentView == RATS_VIEW){
			setRatsView(gl, shaderProgram,WIDTH,HEIGHT,canvas,r);
		}
		let x1= HEIGHT -.5;
		let y1= WIDTH -.5;
		gl.uniformMatrix4fv(modelViewMatrixUniformLocation, false, identityMatrix);
		gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);
		drawTriangle(gl, shaderProgram, y1 +.3, x1+0,y1+-.2,x1+.1,y1+-.2,x1+-.1,[1,1,0,1]);
		if(currentView == TOP_VIEW){
			m.draw(gl, shaderProgram);
		}else{
			m.drawOptimized(gl, shaderProgram);
		}
		// m.drawPath(gl, shaderProgram);
		r.draw(gl, shaderProgram);
		
		requestAnimationFrame(redraw);
	}
	requestAnimationFrame(redraw);
};

function setObserveView(gl, shaderProgram,WIDTH,HEIGHT,canvas){
	const projectionMatrix = mat4.create();
	const fov = 90 * Math.PI / 180;
	const canvasAspect = canvas.clientWidth / canvas.clientHeight
	const near = 1;
	const far = 20;
	mat4.perspective(projectionMatrix, fov, canvasAspect, near, far);

	
	const lookAtMatrix = mat4.create();
	const eye = [WIDTH/2+.1,-HEIGHT/5, WIDTH];
	const at = [WIDTH/2,HEIGHT/2,0];
	const up = [0,0,1];
	mat4.lookAt(lookAtMatrix, eye, at, up);
	mat4.multiply(projectionMatrix, projectionMatrix, lookAtMatrix);
	const projectionMatrixUniformLocation = gl.getUniformLocation(shaderProgram, "uProjectionMatrix");
	gl.uniformMatrix4fv(projectionMatrixUniformLocation, false, projectionMatrix);
	
}

function setTopView(gl, shaderProgram,WIDTH,HEIGHT,canvas){
	const margin = 0.5;
	let xlow = 0.0-margin;
	let xhigh = WIDTH+margin;
	let ylow = 0.0-margin;
	let yhigh = HEIGHT+margin;
	const projectionMatrixUniformLocation = gl.getUniformLocation(shaderProgram, "uProjectionMatrix");
	const projectionMatrix = mat4.create();
	const aspect = canvas.clientWidth / canvas.clientHeight;
	const width = xhigh-xlow;
	const height = yhigh-ylow;
	if (aspect >= width/height){
		const newWidth = aspect*height;
		const xmid = (xlow+xhigh)/2;
		const xlowNew = xmid - newWidth/2;
		const xhighNew = xmid + newWidth/2;
		mat4.ortho(projectionMatrix, xlowNew, xhighNew, ylow, yhigh, -1, 1);
	}
	else{
		const newHeight = width/aspect;
		const ymid = (ylow+yhigh)/2;
		const ylowNew = ymid - newHeight/2;
		const yhighNew = ymid + newHeight/2;
		mat4.ortho(projectionMatrix, xlow, xhigh, ylowNew, yhighNew, -1, 1);
	}

	gl.uniformMatrix4fv(projectionMatrixUniformLocation, false, projectionMatrix);

}

function setRatsView(gl, shaderProgram,WIDTH,HEIGHT,canvas,rat){
	const projectionMatrix = mat4.create();
	const fov = 40 * Math.PI / 180;
	const canvasAspect = canvas.clientWidth / canvas.clientHeight
	const near = 1;
	const far = 20;
	mat4.perspective(projectionMatrix, fov, canvasAspect, near, far);

	
	const lookAtMatrix = mat4.create();
	const eye = [rat.x,rat.y, .5];
	const at = [rat.x+Math.cos(rat.degrees*Math.PI/180),rat.y+Math.sin(rat.degrees*Math.PI/180),.5];
	const up = [0,0,1];
	mat4.lookAt(lookAtMatrix, eye, at, up);
	mat4.multiply(projectionMatrix, projectionMatrix, lookAtMatrix);

	// Move the eye position back a little
	const eyeOffset = vec3.create();

	const projectionMatrixUniformLocation = gl.getUniformLocation(shaderProgram, "uProjectionMatrix");
	gl.uniformMatrix4fv(projectionMatrixUniformLocation, false, projectionMatrix);
	
}
function loadTexture(gl, url) {
	const texture = gl.createTexture();
	gl.bindTexture(gl.TEXTURE_2D, texture);
  
	// Fill the texture with a 1x1 blue pixel while waiting for the image to load
	gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA, 1, 1, 0, gl.RGBA, gl.UNSIGNED_BYTE, new Uint8Array([0, 0, 255, 255]));
  
	const image = new Image();
	image.onload = function () {
	  gl.bindTexture(gl.TEXTURE_2D, texture);
	  gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA, gl.RGBA, gl.UNSIGNED_BYTE, image);
	  gl.generateMipmap(gl.TEXTURE_2D);
	};
	image.src = url;
  
	return texture;
  }
  