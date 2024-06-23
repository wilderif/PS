// 두_큐_합_같게_만들기

const solution = (queue1, queue2) => {
  let ptr1 = 0;
  let ptr2 = 0;
  let sum1 = queue1.reduce((acc, cur) => {
    return (acc += cur);
  }, 0);
  let sum2 = queue2.reduce((acc, cur) => {
    return (acc += cur);
  }, 0);

  let check = queue1.length;

  let cnt = 0;
  while (sum1 !== sum2) {
    cnt++;
    if (sum1 > sum2) {
      if (ptr1 === queue1.length) {
        return -1;
      }
      sum2 += queue1[ptr1];
      sum1 -= queue1[ptr1];
      queue2.push(queue1[ptr1++]);
    } else {
      if (ptr2 === queue2.length) {
        return -1;
      }
      sum1 += queue2[ptr2];
      sum2 -= queue2[ptr2];
      queue1.push(queue2[ptr2++]);
    }
    if (ptr1 >= check * 2) {
      return -1;
    }
  }
  return cnt;
};
