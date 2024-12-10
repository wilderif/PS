// 연속된_수의_합

function solution(num, total) {
  const res = [];
  let tmp = 0;
  if (num % 2) {
    tmp = total / num - Math.floor(num / 2);
  } else {
    tmp = Math.floor(total / num) - num / 2 + 1;
  }
  console.log(tmp);
  for (let i = 0; i < num; i++) {
    res.push(tmp + i);
  }

  return res;
}
