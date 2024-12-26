// 두_정수_사이의_합

function solution(a, b) {
  let res = 0;
  if (b < a) {
    let tmp = a;
    a = b;
    b = tmp;
  }
  for (let i = a; i <= b; i++) {
    res += i;
  }
  return res;
}
