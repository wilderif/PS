// 숨어있는_숫자의_덧셈_(2)

function solution(my_string) {
  let res = 0;
  tmp = "";
  for (let c of my_string) {
    if (!isNaN(c)) {
      tmp += c;
    } else {
      res += Number(tmp);
      tmp = "";
    }
  }
  res += Number(tmp);
  return res;
}
