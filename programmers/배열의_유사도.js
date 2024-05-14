// 배열의_유사도

function solution(s1, s2) {
  var answer = 0;
  for (string1 of s1) {
    for (string2 of s2) {
      if (string1 === string2) {
        answer++;
      }
    }
  }
  return answer;
}
