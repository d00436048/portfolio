import {drawLineLoop,drawCircle, drawRectangle, drawTriangle} from "./shapes2d.js";

class Rat{
    constructor(x,y, angle, maze){
        this.x = x;
        this.y = y;
        this.degrees = angle;
        this.currentDirection = this.calculateDirection();
        this.vertices = [.3,0,-.2,.1,-.2,-.1];
        this.maze = maze;
        this.FATNESS =.3;
        this.SPIN_SPEED = 90;
        this.MOVE_SPEED =1.0;
        this.RADIUS =.07;
    }
    draw(gl, shaderProgram){
        const modelViewMatrixUniformLocation= gl.getUniformLocation(shaderProgram, "uModelViewMatrix");
        const modelViewMatrix = mat4.create();
        mat4.translate(modelViewMatrix, modelViewMatrix, [this.x, this.y, 0]);
        mat4.rotate(modelViewMatrix, modelViewMatrix, this.degrees*Math.PI/180, [0,0,1]);
        gl.uniformMatrix4fv(modelViewMatrixUniformLocation, false, modelViewMatrix);
        
        drawTriangle(gl, shaderProgram, .3,0,-.2,.1,-.2,-.1,[.5,.5,.5,1]);

        drawRectangle(gl, shaderProgram, .2, -.02, .3, .02, [1, 1, 1, 1]);

        drawCircle(gl, shaderProgram, .1, -.1, this.RADIUS, [1,1,1,1]);
        drawCircle(gl, shaderProgram, .1, -.1, .03, [0,0,0,1]);
        drawCircle(gl, shaderProgram, .1, .1, this.RADIUS, [1,1,1,1]);
        drawCircle(gl, shaderProgram, .1, .1, .03, [0,0,0,1]);
        drawRectangle(gl, shaderProgram, -.2, -.01, -.5, .01, [0.6, 0.4, 0.2, 1]);

    }
    calculateDirection() {
        const radians = this.degrees * Math.PI / 180;
        if (radians >= 0 && radians < Math.PI / 2) {
            return 'right';
        } else if (radians >= Math.PI / 2 && radians < Math.PI) {
            return 'up';
        } else if (radians >= -Math.PI && radians < -Math.PI / 2) {
            return 'left';
        } else if (radians >= -Math.PI / 2 && radians < 0) {
            return 'down';
        }
        return 'unknown'; // Fallback direction
    }
    
    spinLeft(DT){
        this.degrees += this.SPIN_SPEED * DT;
        this.calculateDirection();
    }
    spinRight(DT){
        this.degrees -= this.SPIN_SPEED * DT;
        
    }
    scurryForward(DT){

        const dx = Math.cos(this.degrees*Math.PI/180) * this.MOVE_SPEED * DT;
        const dy = Math.sin(this.degrees*Math.PI/180) * this.MOVE_SPEED * DT;
        const newx= this.x + dx;
        const newy= this.y + dy;
        if(this.maze.isSafe(newx,newy,this.FATNESS)){
        this.x = newx;
        this.y= newy;
        }else if(this.maze.isSafe(newx,this.y,this.FATNESS)){
            this.x = newx;
            
        }else if(this.maze.isSafe(this.x,newy,this.FATNESS)){
            this.y= newy;
        }

        
    }
    scurryBackward(DT){
        this.scurryForward(-DT);
    }
    strafeRight(DT){
        const dx = Math.cos((this.degrees-90)*Math.PI/180) * this.MOVE_SPEED * DT;
        const dy = Math.sin((this.degrees-90)*Math.PI/180) * this.MOVE_SPEED * DT;
        const newx= this.x + dx;
        const newy= this.y + dy;
        if(this.maze.isSafe(newx,newy,this.FATNESS)){
        this.x = newx;
        this.y= newy;
        }
        
    }
    strafeLeft(DT){
        const dx = Math.cos((this.degrees+90)*Math.PI/180) * this.MOVE_SPEED * DT;
        const dy = Math.sin((this.degrees+90)*Math.PI/180) * this.MOVE_SPEED * DT;
        const newx= this.x + dx;
        const newy= this.y + dy;
        if(this.maze.isSafe(newx,newy,this.FATNESS)){
        this.x = newx;
        this.y= newy;
        }
        
    }
}
export {Rat};