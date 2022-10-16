/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function(head, n) {
    let temp = head;
    let counter = 0;
    while (temp) {
        temp = temp.next;
        ++counter;
    };
    // Time complexity O(N?) Space complexity O(1)
    // The best solution would require two pointers
    if (counter != n) {
        temp = eval("head" + ".next".repeat(counter - n - 1));
    } else {
        head = head.next;
        return head;
    };
    temp.next = temp.next.next;
    
    return head;
};