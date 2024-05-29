// 컨트롤_제트

function solution(s) {
  let res = [];
  s = s.split(" ");
  for (let i = 0; i < s.length; i++) {
    if (s[i] === "Z") {
      res.pop();
    } else {
      res.push(Number(s[i]));
    }
  }
  return res.reduce((acc, cur) => acc + cur, 0);
}
