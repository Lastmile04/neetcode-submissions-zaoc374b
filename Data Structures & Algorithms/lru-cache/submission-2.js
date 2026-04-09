// Intuition
// <!-- Describe your first thoughts on how to solve this problem. -->
/*
The get and put operations are typical hashmap operations, the thing to manage is the removal of least recently used key when the cache length is exceeded
both get and put are O(1) meaning hashmap, the main point or hint in this problem that gives us the right data structure to use along with hashmap is that we
can use a simple array list to perform operations by iterating through list to erase and insert these key-value pairs. but the time complexity will be O(n) and
caches are meant to be fast and the problem requires us to do all this in O(1) time complexity, which leads to linked list being used to allow removal and reinsertion 
of elements in O(1) time. 
*/

// Approach
/**
 * The basic approch can be like using hashmap for associating key with it's values,  where I can make each value associated with it's key in hashmap a pointer to 
 * node in linked list.
 * 
 * The structure of the linked list is a doubly linked list, having two ends leftmost being the dummy node to build and for easire removal, while the rightmost node also being
 * a dummy node for faster identification and reiteration of the recently used node, whenever an operation like get is called the node we retrieve becomes the 
 * recently used one and is removed and then reinserted at the end. 
 * the capacity removal is simple just make sure to remove the LRU when out of capacity.
 * 
 */

// time complexity


// space complexity



class Node{
    constructor(key, val){
        this.key = key;
        this.val = val;
        this.prev = null;
        this.next = null;
    }
}

class LRUCache {
    /**
     * @param {number} capacity
     */
        constructor(capacity) {
            this.cap = capacity;
            this.cache = new Map();
            // create left and right dummy nodes and connect them together 
            this.left = new Node(0, 0);
            this.right = new Node(0, 0);
            this.left.next = this.right;
            this.right.prev = this.left;
        }

        remove(node){
            const prev = node.prev;
            const nxt = node.next;
            prev.next = nxt;
            nxt.prev = prev;
        }

        insert(node){
            // rightmost dummy node prev or the currnet LRU
            const prev = this.right.prev;

            // inserting new node at the end making connection with the curr LRU
            prev.next = node;
            node.prev = prev;

            // changing current LRU and connecting with rightmost dummy node
            node.next = this.right;
            this.right.prev = node;
        }

        /**
         * @param {number} key
         * @return {number}
         */
        get(key) {
            if (!this.cache.has(key)) return -1;

            const node = this.cache.get(key);
            this.remove(node);
            this.insert(node);
            return node.val;
        }

        /**
         * @param {number} key
         * @param {number} value
         * @return {void}
         */
        put(key, value) {
            if (this.cache.has(key)) {
            const node = this.cache.get(key);
            node.val = value;
            this.remove(node);
            this.insert(node);
            return;
        }

        const newNode = new Node(key, value);
        this.cache.set(key, newNode);
        this.insert(newNode);

        if (this.cache.size > this.cap) {
            const lru = this.left.next;
            this.remove(lru);
            this.cache.delete(lru.key);
            }

        }   
}
