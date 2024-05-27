// 숫자_찾기

function solution(num, k) {
  let res = -1;
  num
    .toString()
    .split("")
    .forEach((n, i) => {
      if (Number(n) === k && res === -1) {
        res = i + 1;
      }
    });
  return res;
}
