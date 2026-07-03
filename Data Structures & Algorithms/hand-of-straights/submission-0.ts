class Solution {
    /**
     * @param {number[]} hand
     * @param {number} groupSize
     * @return {boolean}
     */
    isNStraightHand(hand: number[], groupSize: number): boolean {
        if (hand.length % groupSize !== 0) return false;
        hand.sort((a, b) => a - b);
        const freqMap: Map<number, number> = new Map();
        for (const card of hand) {
            freqMap.set(card, (freqMap.get(card) || 0) + 1);
        }

        for (const card of hand) {
            if (freqMap.get(card) === 0) continue;

            for (let i = 0; i < groupSize; i++) {
                const currCard = card + i;
                const currFreq = freqMap.get(currCard) ?? 0;

                if (currFreq === 0) return false;

                freqMap.set(currCard, currFreq - 1);
            }
        }

        return true;
    }
}
