// 개미_군단

function solution(hp) {
  var answer = 0;
  let mem = new Array(1001).fill(0);
  mem[1] = 1;
  mem[2] = 2;
  mem[3] = 1;
  mem[4] = 2;
  mem[5] = 1;
  for (let i = 6; i < 1001; i++) {
    mem[i] = Math.min(mem[i - 1], mem[i - 3], mem[i - 5]) + 1;
  }
  answer = mem[hp];
  return answer;
<<<<<<< HEAD
}
=======
}
>>>>>>> 5ae11d8804eca0ee95680c2228111cdb04fcc3ac
