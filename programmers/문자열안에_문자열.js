// 문자열안에_문자열

function solution(str1, str2) {
  var answer = 0;
  for (let i = 0; i < str1.length - str2.length + 1; i++) {
    for (let j = 0; j < str2.length; j++) {
      if (str1[i + j] !== str2[j]) {
        break;
      }
      if (j === str2.length - 1) {
        return 1;
      }
    }
  }
  return 2;
}
