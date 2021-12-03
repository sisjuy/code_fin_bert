let str = document.getElementById("str");
let result;
result = str.innerHTML.replace(/Lorem Ipsum/gi, `<span class="my-span">Lorem Ipsum</span>`);
str.innerHTML = result;
console.log(str);