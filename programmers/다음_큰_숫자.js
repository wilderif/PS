// 다음_큰_숫자

const solution = (n) => {
  const cntOne = (binary) => {
    let ret = binary.reduce((acc, cur) => {
      return cur === "1" ? acc + 1 : acc;
    }, 0);
    return ret;
  };

  let target = cntOne(n.toString(2).split(""));
  while (1) {
    if (cntOne((++n).toString(2).split("")) === target) {
      return n;
    }
  }
};
