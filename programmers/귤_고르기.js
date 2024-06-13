// 귤_고르기

const solution = (k, tangerine) => {
  let cont = {};
  tangerine.forEach((val) => {
    if (val in cont) {
      cont[val] += 1;
    } else {
      cont[val] = 1;
    }
  });

  const sortedVal = Object.values(cont).sort((a, b) => b - a);
  let cur = 0;
  let idx = 0;
  while (cur < k) {
    cur += sortedVal[idx++];
  }
  return idx;
};
