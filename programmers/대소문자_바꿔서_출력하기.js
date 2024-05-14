// 대소문자_바꿔서_출력하기

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
    for (let c of str) {
        if (c === c.toLowerCase()) {
            process.stdout.write((c.toUpperCase()));
        } else {
            process.stdout.write((c.toLowerCase()));
        }
    }
<<<<<<< HEAD
});
=======
});
>>>>>>> 5ae11d8804eca0ee95680c2228111cdb04fcc3ac
