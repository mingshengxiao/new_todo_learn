$(function() {
/*
	函数、函数对象、本地对象、内置对象、宿主对象
*/
	function foo(){

	}  // 函数声明

	var foo = function() {

	}  // 函数表达式

	function Person() {

	}
	Person.prototype.name = "tom";
	Person.prototype.age = 18;
	Person.prototype.jon = "student";
	Person.prototype.sayName = function() {
		alert(this.name);
	}

	var person1 = new Person()  // person1.__proto__ === Foo.prototype
	person1.sayName()  // tom

	var person2 = new Person()
	person2.sayName()  // tom

	// alert(person1.sayName == person2.sayName)  // true

	// 每个构造函数都有一个原型对象，原型对象都包含一个指向构造函数的指针，实例都包含一个指向原型对象的内部指针

	// js中通过原型实现继承

		
})