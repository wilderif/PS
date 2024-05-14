// 최댓값_만들기_(2)

function solution(numbers) {
  var answer = numbers[0] * numbers[1];
  for (let i = 0; i < numbers.length; i++) {
    for (let j = i + 1; j < numbers.length; j++) {
      answer = Math.max(answer, numbers[i] * numbers[j]);
    }
  }

  return answer;
}
