// 2_x_n_타일링

const solution = (n) => {
  let mem = new Array(n + 5);
  mem[1] = 1;
  mem[2] = 2;
  for (let i = 3; i < n + 1; i++) {
    mem[i] = (mem[i - 1] + mem[i - 2]) % 1000000007;
  }

  return mem[n];
};
