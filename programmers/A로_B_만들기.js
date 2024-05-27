// A로_B_만들기

function solution(before, after) {
  before = before.split("").sort().join("");
  after = after.split("").sort().join("");
  if (before === after) {
    return 1;
  } else {
    return 0;
  }
}
