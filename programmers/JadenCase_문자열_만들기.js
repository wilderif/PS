// JadenCase_문자열_만들기

const solution = (s) => {
  let res = "";
  s = " " + s;

  for (let i = 1; i < s.length; i++) {
    if (s[i - 1] == " ") {
      if (!isNaN(s[i])) {
        res += s[i];
      } else {
        res += s[i].toUpperCase();
      }
    } else {
      res += s[i].toLowerCase();
    }
  }
  return res;
};
