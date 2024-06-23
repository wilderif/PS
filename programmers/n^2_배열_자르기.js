// n^2_배열_자르기

const solution = (n, left, right) => {
  let res = [];
  for (let i = Math.floor(left / n); i < Math.floor(right / n) + 1; i++) {
    for (let j = 0; j < n; j++) {
      if (left <= i * n + j && i * n + j <= right) {
        tmp = Math.max(i, j) + 1;
        res.push(tmp);
      }
    }
  }
  return res;
};
