import {drawColorVertices, drawLine,drawQuad, drawVertices3d,storeQuad} from "./shapes2d.js";

class Cell{
    constructor(){
        this.left = true;
        this.bottom = true;
        this.right = true;
        this.top = true;
        this.visited = false;
    }

    draw(gl, shaderProgram, x,y){
        //draw 2d
        const vertices = [];
        if (this.left){
            vertices.push(x,y, x, y+1);
        }
        if (this.bottom){
            vertices.push(x,y, x+1,y);
        }
        if(this.top){
            vertices.push(x, y+1, x+1, y+1);
        }       
        if(this.right){
            vertices.push(x+1, y, x+1, y+1);
        }
        drawLine(gl, shaderProgram, vertices);
    // }

    //draw 3d
    // const vertices = [];
}
drawOptimized(gl, shaderProgram, x, y, vertices){
    let H=1;
		let u1=0; let v1=H;
		let u2=H; let v2=H;
		let u3=H; let v3=0;
		let u4=0; let v4=0;

    // Draw walls as 3D quads:
    if (this.left) {
        storeQuad(vertices, x, y, 0, u1, v1, x, y + 1, 0, u2, v2, x, y + 1, 1, u3, v3, x, y, 1, u4, v4);
    }
    if (this.right) {
        storeQuad(vertices, x + 1, y, 0, u1, v1, x + 1, y + 1, 0, u2, v2, x + 1, y + 1, 1, u3, v3, x + 1, y, 1, u4, v4);
    }
    if (this.bottom) {
        storeQuad(vertices, x, y, 0, u1, v1, x + 1, y, 0, u2, v2, x + 1, y, 1, u3, v3, x, y, 1, u4, v4);
    }
    if (this.top) {
        storeQuad(vertices, x, y + 1, 0, u1, v1, x + 1, y + 1, 0, u2, v2, x + 1, y + 1, 1, u3, v3, x, y + 1, 1, u4, v4);
    }
}
    
}

class Maze{
    constructor(width, height){
        this.width = width;
        this.height = height;
        this.cells =[];
        
        for(let r = 0; r < this.height; r++){
            this.cells[r] = [];
            for(let c = 0; c < this.width; c++){
                this.cells[r].push(new Cell());
            }
        }
        // this.createMaze();
        this.RemoveWalls(0,0);
        this.cells[0][0].bottom = false;
        this.cells[this.height-1][this.width-1].top = false;
    }
    isSafe(x,y,radius){
        const c = Math.floor(x);
        const r = Math.floor(y);
        const offsetX = x - c;
        const offsetY = y - r;
        if(c >= this.width || r >= this.height || c < 0 || r < 0){
            return true;
        }
        if(this.cells[r][c].right && offsetX + radius > 1.0){
            return false;
        }
        if(this.cells[r][c].left && offsetX - radius < 0.0){
            return false;
        }
        if(this.cells[r][c].top && offsetY + radius > 1.0){
            return false;
        }
        if(this.cells[r][c].bottom && offsetY - radius < 0.0){
            return false;
        }
        if(offsetX + radius >1 && offsetY - radius < 0){
            return false;
        }
        if(offsetX - radius <0 && offsetY - radius < 0){
            return false;
        }
        if(offsetX + radius >1 && offsetY + radius > 1){
            return false;
        }
        if(offsetX - radius <0 && offsetY + radius > 1){
            return false;
        }
        return true;


    }
    

    
    
    createMaze() {
        // Initialize all cells

        // Manually configure the maze with a predefined path
        // Top row
        // this.cells[0][0].top =true;
       this.cells[0][1].top=false; // Path between (1,2) and (2,2)
       this.cells[1][1].bottom=false; // Path between (1,2) and (2,2)

        // Bottom row is already isolated by default walls

        // Mark all as visited for drawing
        // for (let r = 0; r < this.height; r++) {
        //     for (let c = 0; c < this.width; c++) {
        //         this.cells[r][c].visited = true;
        //     }
        // }

        
    }
    RemoveWalls(r, c){
        this.cells[r][c].visited = true;
        const left = 0;
        const bottom = 1;
        const right = 2;
        const top = 3; // Correctly declare the 'top' direction
        let possibilities = [];
        while (true){
            possibilities = [];
            if (c > 0 && !this.cells[r][c - 1].visited) {
                possibilities.push(left);
            }
            if (r >0 && !this.cells[r - 1][c].visited) {
                possibilities.push(bottom);
            }
            if (c < this.width - 1 && !this.cells[r][c + 1].visited) {
                possibilities.push(right);
            }
            if (r < this.height -1  && !this.cells[r + 1][c].visited) {
                possibilities.push(top);
            } 

            if (possibilities.length == 0) {
                return; // Correct way to break out when there are no more cells to visit
            }

            const randomIndex = Math.floor(Math.random() * possibilities.length);
            const direction = possibilities[randomIndex];

            switch (direction) {
                case left:
                    if (c > 0) {
                        this.cells[r][c].left = false;
                        this.cells[r][c - 1].right = false;
                        console.log("left");
                        this.RemoveWalls(r, c - 1);
                    }
                    break;
                case bottom:
                    if (r >0) {
                        this.cells[r][c].bottom = false;
                        this.cells[r - 1][c].top = false;
                        console.log("bottom");
                        this.RemoveWalls(r - 1, c);
                    }
                    break;
                case right:
                    if (c < this.width - 1) {
                        this.cells[r][c].right = false; // Corrected to remove the right wall
                        this.cells[r][c + 1].left = false;
                        console.log("right");
                        this.RemoveWalls(r, c + 1);
                    }
                    break;
                case top:
                    if (r < this.height-1) {
                        this.cells[r][c].top = false; // Corrected to remove the top wall
                        this.cells[r + 1][c].bottom = false;
                        console.log("top");
                        this.RemoveWalls(r + 1, c);
                    }
                    break;
            
            }
        }
    }
    
    draw(gl, shaderProgram){
        for(let r=0; r<this.height; r++){
            for(let c= 0; c<this.width; c++){
                this.cells[r][c].draw(gl, shaderProgram, c,r);
            }
        }
    }
    drawOptimized(gl, shaderProgram){
        let vertices = [];
        for(let r=0; r<this.height; r++){
            for(let c=0; c<this.width; c++){
                this.cells[r][c].drawOptimized(gl, shaderProgram, c, r, vertices);
            }
        }
        drawColorVertices(gl, shaderProgram, vertices, gl.TRIANGLES);
    }
}

export {Maze};