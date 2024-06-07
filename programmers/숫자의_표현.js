// 숫자의_표현

function solution(n) {
  let res = 0;
  for (let i = 1; i < n + 1; i++) {
    if (!(n % i) && i % 2) {
      res++;
    }
  }

  return res;
}
