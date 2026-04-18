class MinStack {
    constructor() {
		this.stack = [];
		this.min = [];
	}

    /**
     * @param {number} val
     * @return {void}
     */
    push(val) {
		if(this.isEmpty()){
			this.stack.push(val);
			this.min.push(val);
		}else{
			this.stack.push(val);
			if(val <= this.min[this.min.length - 1]) this.min.push(val);
		}
	}

    /**
     * @return {void}
     */
    pop() {
		if(this.isEmpty()) return 'Empty Stack';
		const pop = this.stack.pop();
		if(pop === this.min[this.min.length -1]) this.min.pop();			
	}

    /**
     * @return {number}
     */
    top() {
		if(this.isEmpty()) return 'Empty Stack';
		return this.stack[this.stack.length -1];
	}

    /**
     * @return {number}
     */
    getMin() {
		if(this.isEmpty()) return -1;
		return this.min[this.min.length - 1];
	}
	
	isEmpty() { return this.stack.length === 0; }
}
