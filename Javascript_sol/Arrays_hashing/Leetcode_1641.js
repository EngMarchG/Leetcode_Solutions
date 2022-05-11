/**
 * @param {number} n
 * @return {number}
 */
// n=1 is the base case
// Time Complexity: O(10*len(arr)*n) ; Space Complexity: O(1)
// After the base case, the value at pos i is the sum of the terms
// after it
var countVowelStrings = function(n) {
    let arr = [1, 1, 1, 1, 1];
    for (num = 1; num < n; num++) {
        for (i = 0; i < arr.length ; i++) {
            let total = 0
            for (j = i; j < arr.length ; j++ ) {
                total += arr[j]
            }
            arr[i] = total
        }
    }
    return arr.reduce((a, v)=>a + v)
};