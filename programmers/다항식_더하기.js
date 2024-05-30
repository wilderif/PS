// 다항식_더하기

function solution(polynomial) {
  let arr = polynomial.split(" + ").reduce(
    (acc, cur) => {
      if (cur[cur.length - 1] === "x") {
        acc[0] += Number(cur.slice(0, -1) || 1);
      } else {
        acc[1] += Number(cur);
      }
      return acc;
    },
    [0, 0]
  );

  let res = "";
  if (arr[0] === 0) {
    return arr[1] + "";
  } else {
    if (arr[0] === 1) {
      res += "x";
    } else {
      res += arr[0] + "x";
    }
  }
  return res + (arr[1] === 0 ? "" : " + " + arr[1]);
}
