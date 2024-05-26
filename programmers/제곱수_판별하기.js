// 제곱수_판별하기

function solution(n) {
  if (Number.isInteger(Math.sqrt(n))) {
    return 1;
  }
  return 2;
}
