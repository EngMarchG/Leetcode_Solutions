/**
 * @param {string[]} strs
 * @return {string[][]}
 */
 var groupAnagrams = function(strs) {
  let hmap = {};
  let arr = [];
  let counter = 1;
  
  strs.forEach((ele) => {
      let vars = ele.split("").sort().join("");
      
      if (hmap[vars]) {
          arr[hmap[vars]-1].push(ele);
      } else {
          hmap[vars] = counter;
          arr.push([ele])
          ++counter;
      };
      
  });
  
  return arr;
};