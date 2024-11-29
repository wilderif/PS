// OX퀴즈

function solution(quiz) {
  const res = [];
  for (s of quiz) {
    s = s.split(" ");
    let tmp = 0;
    tmp = Number(s[0]);
    if (s[1] === "+") {
      tmp += Number(s[2]);
    }
    if (s[1] === "-") {
      tmp -= Number(s[2]);
    }
    if (tmp === Number(s[4])) {
      res.push("O");
    } else {
      res.push("X");
    }
  }
  return res;
}
