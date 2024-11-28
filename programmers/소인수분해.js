// 소인수분해

function solution(n) {
  let res = [];
  let divisor = 2;

  while (n !== 1) {
    if (n % divisor === 0) {
      if (res[res.length - 1] !== divisor) {
        res.push(divisor);
      }
      n /= divisor;
    } else {
      divisor += 1;
    }
  }

  return res;
}
