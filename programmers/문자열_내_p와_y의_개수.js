// 문자열_내_p와_y의_개수

function solution(s){
  var answer = true;

  let res = 0;
  for (let c of s) {
    if (c === 'p' || c === 'P') {
      res++;
    }
    if (c === 'y' || c === 'Y') {
      res--;
    }
  }
  if (res !== 0) {
    answer = false;
  }

  return answer;
<<<<<<< HEAD
}
=======
}
>>>>>>> 5ae11d8804eca0ee95680c2228111cdb04fcc3ac
