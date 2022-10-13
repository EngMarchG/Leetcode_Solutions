/**
 * @param {string} num1
 * @param {string} num2
 * @return {string}
 */
 var multiply = function(num1, num2) {
  // Big int is necessary to handle extreme number multiplications properly
  return (BigInt(num1)*BigInt(num2)) + "";
};