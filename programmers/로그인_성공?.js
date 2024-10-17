// 로그인_성공?

function solution(id_pw, db) {
  let res = "fail";

  for (let data of db) {
    if (id_pw[0] === data[0]) {
      res = "wrong pw";
      if (id_pw[1] === data[1]) {
        res = "login";
        break;
      }
    }
  }

  return res;
}
