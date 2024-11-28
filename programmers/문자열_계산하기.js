// 문자열_계산하기

function solution(my_string) {
  my_string = my_string.split(" ");
  let res = Number(my_string[0]);

  for (let i = 1; i < my_string.length; i++) {
    if (my_string[i] === "+") {
      res += Number(my_string[i + 1]);
    }
    if (my_string[i] === "-") {
      res -= Number(my_string[i + 1]);
    }
  }

  return res;
}
