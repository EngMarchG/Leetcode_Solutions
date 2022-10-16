/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var sortList = function(head) {
    let temp = head;
    let arr = [];
    
    //Time complexity O(3N)=O(N) Space complexity O(N)
    while (temp) {
        arr.push(temp.val);
        temp = temp.next;
    };
    
    // Don't just use .sort!!!
    arr.sort((a, b) => {
  return a - b;
});
    temp = head;
    
    arr.forEach(num => {
        temp.val = num;
        temp = temp.next;
    });
    return head;
};