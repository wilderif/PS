// 의상

const solution = (clothes) => {
  let obj = {};
  clothes.forEach((val) => {
    if (val[1] in obj) {
      obj[val[1]].push(val[0]);
    } else {
      obj[val[1]] = [val[0]];
    }
  });

  let res = 1;
  Object.values(obj).forEach((val) => {
    res *= val.length + 1;
  });
  return res - 1;
};
