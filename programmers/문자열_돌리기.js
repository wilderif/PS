// 문자열_돌리기

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
    let arr = [...str];
    console.log(arr.join('\n'));
<<<<<<< HEAD
});
=======
});
>>>>>>> 5ae11d8804eca0ee95680c2228111cdb04fcc3ac
