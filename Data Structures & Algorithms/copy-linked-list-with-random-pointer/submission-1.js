// class Node {
//   constructor(val, next = null, random = null) {
//       this.val = val;
//       this.next = next;
//       this.random = random;
//   }
// }

class Solution {
    /**
     * @param {Node} head
     * @return {Node}
     */
    copyRandomList(head) {
        const map = new Map();
        map.set(null, null);

        let curr = head;
        while (curr !== null) {

            if(!map.has(curr)) map.set(curr, new Node(0));
            map.get(curr).val = curr.val;

            if(!map.has(curr.next)) map.set(curr.next, new Node(0));
            map.get(curr).next = map.get(curr.next);

            if(!map.has(curr.random)) map.set(curr.random, new Node(0));
            map.get(curr).random = map.get(curr.random);

            curr = curr.next;
        }
        return map.get(head);
    }
}
