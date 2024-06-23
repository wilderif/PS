// 뒤에_있는_큰_수_찾기

const solution = (numbers) => {
  let res = new Array(numbers.length).fill(-1);
  let stack = [];
  for (let i = 0; i < numbers.length; i++) {
    while (stack.length && stack[stack.length - 1][0] < numbers[i]) {
      let tmp = stack.pop();
      res[tmp[1]] = numbers[i];
    }
    stack.push([numbers[i], i]);
  }
  return res;
};
