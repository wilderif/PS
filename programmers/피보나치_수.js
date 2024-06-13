// 피보나치_수

function solution(n) {
  let mem = new Array(n + 1).fill(0);
  mem[0] = 0;
  mem[1] = 1;
  for (let i = 2; i < n + 1; i++) {
    mem[i] = mem[i - 1] + mem[i - 2];
    mem[i] %= 1234567;
  }

  return mem[n];
}
