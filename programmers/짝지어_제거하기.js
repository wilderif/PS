// 짝지어_제거하기

const solution = (s) => {
  const stack = [];
  s.split("").forEach((c) => {
    if (stack.length && stack[stack.length - 1] == c) {
      stack.pop();
    } else {
      stack.push(c);
    }
  });
  return stack.length ? 0 : 1;
};
