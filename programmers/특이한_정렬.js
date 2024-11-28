// 특이한_정렬

function solution(numlist, n) {
  for (let i = 0; i < numlist.length; i++) {
    if (numlist[i] <= n) {
      numlist[i] = [numlist[i], n - numlist[i]];
    } else {
      numlist[i] = [numlist[i], numlist[i] - n];
    }
  }

  numlist.sort((a, b) => {
    if (a[1] === b[1]) {
      return b[0] - a[0];
    }

    return a[1] - b[1];
  });

  return numlist.map((el) => el[0]);
}
