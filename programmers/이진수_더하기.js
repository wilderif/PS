// 이진수_더하기

function solution(bin1, bin2) {
  bin1 = bin1.split("").reverse();
  bin2 = bin2.split("").reverse();

  const res = [];
  let last = 0;
  for (let i = 0; i < Math.max(bin1.length, bin2.length); i++) {
    let tmp1 = bin1[i] ? Number(bin1[i]) : 0;
    let tmp2 = bin2[i] ? Number(bin2[i]) : 0;
    const tmp = last + tmp1 + tmp2;

    if (tmp === 0) {
      res.push("0");
    }
    if (tmp === 1) {
      res.push("1");
      last = 0;
    }
    if (tmp === 2) {
      res.push("0");
      last = 1;
    }
    if (tmp === 3) {
      res.push("1");
      last = 1;
    }
  }
  if (last) {
    res.push("1");
  }

  return res.reverse().join("");
}
