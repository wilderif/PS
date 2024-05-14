// 문자열_반복해서_출력하기

const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = line.split(' ');
}).on('close', function () {
    str = input[0];
    n = Number(input[1]);
    let res = "";
    while (n--) {
        res += str;
    }
    console.log(res);
<<<<<<< HEAD
});
=======
});
>>>>>>> 5ae11d8804eca0ee95680c2228111cdb04fcc3ac
