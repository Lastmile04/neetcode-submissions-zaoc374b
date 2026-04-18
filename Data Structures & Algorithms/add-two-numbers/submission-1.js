/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 Add Two Numbers
Medium
Topics
Company Tags
Hints
You are given two non-empty linked lists, l1 and l2, where each represents a non-negative integer.

The digits are stored in reverse order, e.g. the number 321 is represented as 1 -> 2 -> 3 -> in the linked list.

Each of the nodes contains a single digit. You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Return the sum of the two numbers as a linked list.
 */

class Solution {
    /**
     * @param {ListNode} l1
     * @param {ListNode} l2
     * @return {ListNode}
     */
    
	add(l1, l2, carry){
		// base case
		if(!l1 && !l2 && carry === 0) return null;
		
		let v1 = 0;
		let v2 = 0;
		
		if(l1) v1 = l1.val;
		if(l2) v2 = l2.val;
		
		let sum = v1 + v2 + carry;
		let newCarry = Math.floor(sum/10);
		let nodeVal = sum % 10;
		
		// traverse the list nodes
		let nextNode = this.add(
			l1 ? l1.next : null,
			l2 ? l2.next : null,
			newCarry,
		);
		
		return new ListNode(nodeVal, nextNode);
		
		
	}
	
	
	addTwoNumbers(l1, l2) {
		return this.add(l1, l2, 0);
		
	}
	
}
