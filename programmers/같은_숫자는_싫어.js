// 같은_숫자는_싫어

function solution(arr) {
  const stack = [];
  for (const el of arr) {
    if (stack.length) {
      if (el === stack[stack.length - 1]) {
        continue;
      } else {
        stack.push(el);
      }
    } else {
      stack.push(el);
    }
  }

  return stack;
}
