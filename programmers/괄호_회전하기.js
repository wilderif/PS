// 괄호_회전하기

const solution = (s) => {
  const check = (s) => {
    stack = [];
    for (let i = 0; i < s.length; i++) {
      if (["(", "{", "["].includes(s[i])) {
        stack.push(s[i]);
      } else if (s[i] === ")" && stack[stack.length - 1] === "(") {
        stack.pop();
      } else if (s[i] === "}" && stack[stack.length - 1] === "{") {
        stack.pop();
      } else if (s[i] === "]" && stack[stack.length - 1] === "[") {
        stack.pop();
      } else {
        stack.push(s[i]);
      }
    }
    return stack.length === 0 ? true : false;
  };

  res = 0;
  s = s.split("");
  for (let i = 0; i < s.length; i++) {
    s.push(s.shift());
    if (check(s)) {
      res++;
    }
  }
  return res;
};
