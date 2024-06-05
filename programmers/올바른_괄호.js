// 올바른_괄호

function solution(s) {
  let arr = [];
  for (const c of s) {
    if (c === ")") {
      if (arr.length) {
        arr.pop();
      } else {
        return false;
      }
    } else {
      arr.push(c);
    }
  }

  return arr.length ? false : true;
}
