// 자릿수_더하기_2

function solution(n) {
  return n
    .toString()
    .split("")
    .reduce((acc, cur) => {
      return acc + Number(cur);
    }, 0);
}
