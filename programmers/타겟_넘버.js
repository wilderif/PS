// 타겟_넘버

const solution = (numbers, target) => {
  let vis = new Array(numbers.length + 1);
  vis[0] = { 0: 1 };
  for (let i = 0; i < numbers.length; i++) {
    let tmp = {};
    for (let key of Object.keys(vis[i])) {
      let intKey = parseInt(key);
      let plusKey = intKey + numbers[i];
      let minusKey = intKey - numbers[i];
      if (plusKey in tmp) {
        tmp[plusKey] += vis[i][key];
      } else {
        tmp[plusKey] = vis[i][key];
      }
      if (minusKey in tmp) {
        tmp[minusKey] += vis[i][key];
      } else {
        tmp[minusKey] = vis[i][key];
      }
    }
    vis[i + 1] = tmp;
  }

  return vis[numbers.length][target];
};
