// 약수_구하기

function solution(n) {
  let arr1 = [];
  let arr2 = [];
  for (let i = 1; i < Math.sqrt(n) + 1; i++) {
    if (n % i === 0) {
      arr1.push(i);
      arr2.push(n / i);
    }
  }

  if (Number.isInteger(Math.sqrt(n))) {
    arr2.pop();
  }
  return arr1.concat(arr2.reverse());
}
