// 겹치는_선분의_길이

function solution(lines) {
  let arr = new Array(201).fill(0);
  for (let line of lines) {
    for (let i = line[0] + 100; i < line[1] + 100; i++) {
      arr[i]++;
    }
  }

  return arr.filter((el) => el > 1).length;
}
