// 저주의_숫자_3

function solution(n) {
  let res = 0;

  const isMultiple = (num) => {
    return num % 3 ? false : true;
  };

  const isInclude = (num) => {
    const tmp = String(num).split("");
    for (c of tmp) {
      if (c === "3") {
        return true;
      }
    }
    return false;
  };

  for (let i = 0; i < n; i++) {
    res += 1;
    while (isMultiple(res) || isInclude(res)) {
      res += 1;
    }
  }

  return res;
}
