// 2차원으로_만들기

function solution(num_list, n) {
  let res = [];
  let tmp = [];
  for (let i = 0; i < num_list.length; i++) {
    if (i % n === 0 && i) {
      res.push(tmp);
      tmp = [];
    }
    tmp.push(num_list[i]);
  }
  res.push(tmp);

  return res;
}
