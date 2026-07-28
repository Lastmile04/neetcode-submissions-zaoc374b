class Solution {
    /**
     * @param {number[]} people
     * @param {number} limit
     * @return {number}
     */
    numRescueBoats(people: number[], limit: number): number {
    people.sort((a, b) => a - b);
    
    let l = 0;
    let r = people.length - 1;
    let boats = 0;
    
    while (l <= r) {
        // If the lightest and heaviest person can share a boat, move the left pointer
        if (people[l] + people[r] <= limit) {
            l++;
        }
        
        // The heaviest person ALWAYS gets a boat (either alone or shared)
        r--;
        boats++;
    }
    
    return boats;
    }
}
