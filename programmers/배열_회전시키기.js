// 배열_회전시키기

function solution(numbers, direction) {
  direction === "right"
    ? numbers.unshift(numbers.pop())
    : numbers.push(numbers.shift());

  return numbers;
}
