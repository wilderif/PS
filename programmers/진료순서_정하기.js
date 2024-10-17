// 진료순서_정하기

function solution(emergency) {
  let res = new Array(emergency.length).fill(0);

  for (let i = 0; i < emergency.length; i++) {
    emergency[i] = [emergency[i], i];
  }

  emergency.sort((a, b) => b[0] - a[0]);

  for (let i = 0; i < emergency.length; i++) {
    res[emergency[i][1]] = i + 1;
  }

  return res;
}
