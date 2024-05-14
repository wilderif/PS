// 외계행성의_나이

function solution(age) {
  var answer = '';
  age = age.toString();
  for (let c of age) {
    answer += String.fromCharCode(c.charCodeAt() - '0'.charCodeAt() + 'a'.charCodeAt());
  }
  return answer;
<<<<<<< HEAD
}
=======
}
>>>>>>> 5ae11d8804eca0ee95680c2228111cdb04fcc3ac
