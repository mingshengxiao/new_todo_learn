$(function() {
	// 单例模式即一个类只能创建一个实例对象
	// 在构造函数的静态属性中缓存该实例，缺点：外部代码可能会修改该属性
	function Universe() {
		if(typeof Universe.instance === 'object'){
			return Universe.instance
		}
		Universe.instance = this
		return this
	}

	var uni1 = new Universe()
	var uni2 = new Universe()
	uni1 === uni2  // true 

	// 闭包 缺点：额外的闭包开销
	function Universe() {
		var instance = this
		Universe = function() {
			return instance
		}
	}

	var uni1 = new Universe()
	var uni2 = new Universe()
	uni1 === uni2  // true  
})