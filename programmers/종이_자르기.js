// 종이_자르기

function solution(M, N) {
  let res = 0;
  res += M - 1;
  res += M * (N - 1);
  return res;
}
