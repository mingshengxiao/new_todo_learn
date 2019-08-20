/*
  给定一个数组和正整数n（n小于数组长度），请将此数组循环左移n个位置。

  eg: 输入：[1,3,5,8,6],3
      输出：[8,6,1,3,5]

*/

// 向左移动n位，则先将数组中arr[n]左边部分进行逆序，再将arr[n]右边部分进行逆序，最后将整个数组进行逆序

//逆序函数
function reverse(arr, left, right) {
  let temp;
  while(left < right) {
    //两数交换
    temp = arr[left];
    arr[left] = arr[right];
    arr[right] = temp;
    //左下标+1，右下标-1
    left++;
    right--;
  }
}

//循环左移函数
//arr：数组
//n：左移位数
function loopLeft(arr, n) {
  if(arr === null || arr.length === 0) return arr;
  //对左半部分进行逆序
  reverse(arr, 0, n - 1);
  //对右半部分进行逆序
  reverse(arr, n, arr.length - 1);
  //对整个数组进行逆序
  reverse(arr, 0, arr.length - 1);
  return arr;
}