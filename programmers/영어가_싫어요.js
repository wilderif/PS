// 영어가_싫어요

function solution(numbers) {
  const dict = {
    zero: "0",
    one: "1",
    two: "2",
    three: "3",
    four: "4",
    five: "5",
    six: "6",
    seven: "7",
    eight: "8",
    nine: "9",
  };

  let res = "";
  let cur = "";
  for (let i = 0; i < numbers.length; i++) {
    cur += numbers[i];
    if (dict[cur]) {
      answer = res += dict[cur];
      cur = "";
    }
  }

  return Number(res);
}
