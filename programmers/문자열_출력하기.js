// 문자열_출력하기

const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = [line];
}).on('close',function(){
    str = input[0];
    console.log(str);
<<<<<<< HEAD
});
=======
});
>>>>>>> 5ae11d8804eca0ee95680c2228111cdb04fcc3ac
