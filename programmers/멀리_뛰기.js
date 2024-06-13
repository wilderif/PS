// 멀리_뛰기

const solution = (n) => {
  let mem = new Array(n + 5).fill(0);
  mem[1] = 1;
  mem[2] = 2;
  for (let i = 3; i < n + 1; i++) {
    mem[i] = mem[i - 1] + mem[i - 2];
    mem[i] %= 1234567;
  }

  return mem[n];
};
