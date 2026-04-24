class Solution {
    /**
     * @param {ListNode} head
     * @return {void}
     */
    reorderList(head) {
        let f = head,
            s = head; 
        while (f !== null && f.next !== null) {
            s = s.next;
            f = f.next.next;        
        }
        
        // find the middle and store the start of the next half
        let half = s.next;
        s.next = null;

        // reverse the remaining half
        let curr = half,
            end = null;

        while(curr){
            let temp = curr.next;
            curr.next = end;
            end = curr;
            curr = temp;
        }

        // merge two lists
        let first = head,
            second = end;
        
        while(second){
            let t1 = first.next,
                t2 = second.next;

            first.next = second;
            second.next = t1;

            [first, second] = [t1, t2];
        }
    }
}
