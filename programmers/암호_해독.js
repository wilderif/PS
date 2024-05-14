// 암호_해독

function solution(cipher, code) {
  var answer = "";
  let idx = code - 1;
  while (idx < cipher.length) {
    answer += cipher[idx];
    idx += code;
  }
  return answer;
}
