// 최솟값_만들기

function solution(A, B) {
  let arr1 = A.sort((a, b) => a - b);
  let arr2 = B.sort((a, b) => b - a);
  let res = 0;
  for (let i = 0; i < arr1.length; i++) {
    res += arr1[i] * arr2[i];
  }

  return res;
}
