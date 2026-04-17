class Node{
	constructor(){
		this.children = new Map();
		this.end = false;
	}
}

class PrefixTree {
    constructor() {
		this.root = new Node();
	}

    /**
     * @param {string} word
     * @return {void}
     */
    insert(word) {
		let node = this.root;
		
		for(let ch of word){
			if(!node.children.has(ch)){
				node.children.set(ch, new Node());
			}
			node = node.children.get(ch);
		}
		node.end = true;
	}

    /**
     * @param {string} word
     * @return {boolean}
     */
    search(word) {
		let node = this.root;
		for(let ch of word){
			if(!node.children.has(ch)){
				return false;
			}
			node = node.children.get(ch);
		}
		return node.end;
	}

    /**
     * @param {string} prefix
     * @return {boolean}
     */
    startsWith(prefix) {
		let node = this.root;
		for(let ch of prefix){
			if(!node.children.has(ch)){
				return false;
			}
			node = node.children.get(ch);
		}
		return true;
	}
}
