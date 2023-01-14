/**
 * @param {number[]} nums
 * @return {string[]}
 */
var summaryRanges = function(nums) {
  let arr = [];
  let counts = 0;

  for (let i=0; i < nums.length-1; i++) {
      for (let j=i+1; j < nums.length; j++) {
          if (nums[j] - nums[i+counts] === 1) {
              counts += 1
          } else {break};
      };

      if (counts) {
          arr.push(`${nums[i]}->${nums[i+counts]}`)
      } else {arr.push(`${nums[i]}`)};
      i += counts;
      counts = 0
  };

  if (nums.length > 1 && `${(arr.at(-1).slice([arr.at(-1).length-nums.at(-1).toString().length]-1))}` != `>${nums[nums.length-1]}`) {
   arr.push(`${nums[nums.length-1]}`)} 
   else if (nums.length>0 && arr.length === 0){
       return [`${nums[0]}`]
   };
  
  return arr;
};