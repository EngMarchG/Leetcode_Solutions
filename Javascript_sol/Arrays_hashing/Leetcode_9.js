/**
 * @param {number} x
 * @return {boolean}
 */

// Convert the integer to a string and initiate a loop
// with 2 pointers till the middle
// Time Complexity: O(2n) ; Space Complexity: O(n)
var isPalindrome = function(x) {
    const y = x.toString()
    const size = y.length;

    for (i=0; i<=Math.ceil(size/2); i++) {
        if (y[i] != y[size-1-i]) {
            return false;
        }
    }
    return true;
};