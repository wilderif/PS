// 잘라서_배열로_저장하기

function solution(my_str, n) {
  let res = [];
  my_str = my_str.split("");

  let tmp = "";
  let cnt = 0;
  for (c of my_str) {
    tmp += c;
    cnt++;
    if (cnt === n) {
      res.push(tmp);
      tmp = "";
      cnt = 0;
    }
  }

  if (tmp.length) {
    res.push(tmp);
  }

  return res;
}
