// 가까운_수

function solution(array, n) {
  let res = 0;
  let diff = 100;
  for (i of array) {
    let tmp = 0;
    if (i < n) {
      tmp = n - i;
    } else if (i === n) {
      return i;
    } else {
      tmp = i - n;
    }

    if (tmp < diff) {
      res = i;
      diff = tmp;
    }
    if (tmp === diff) {
      if (i < n) {
        res = i;
      }
    }
  }

  return res;
}
