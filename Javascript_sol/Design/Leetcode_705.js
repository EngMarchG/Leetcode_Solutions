var MyHashSet = function() {
  this.hmap = {};
};

/** 
* @param {number} key
* @return {void}
*/
MyHashSet.prototype.add = function(key) {
  this.hmap[key] = true
};

/** 
* @param {number} key
* @return {void}
*/
MyHashSet.prototype.remove = function(key) {
  this.hmap[key] = false
};

/** 
* @param {number} key
* @return {boolean}
*/
MyHashSet.prototype.contains = function(key) {
  if (this.hmap[key] != undefined) {return this.hmap[key]};
  return false   
};

/** 
* Your MyHashSet object will be instantiated and called as such:
* var obj = new MyHashSet()
* obj.add(key)
* obj.remove(key)
* var param_3 = obj.contains(key)
*/