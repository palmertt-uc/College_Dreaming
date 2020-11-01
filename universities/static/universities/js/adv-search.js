let slider = document.getElementById("myRange");
let output = document.getElementById("demo");
let slider1 = document.getElementById("myRange1");
let output1 = document.getElementById("demo1");
let slider2 = document.getElementById("myRange2");
let output2 = document.getElementById("demo2");
let slider3 = document.getElementById("myRange3");
let output3 = document.getElementById("demo3");
let slider4 = document.getElementById("myRange4");
let output4 = document.getElementById("demo4");
let slider5 = document.getElementById("myRange5");
let output5 = document.getElementById("demo5");
let slider6 = document.getElementById("myRange6");
let output6 = document.getElementById("demo6");
let slider7 = document.getElementById("myRange7");
let output7 = document.getElementById("demo7");
let slider8 = document.getElementById("myRange8");
let output8 = document.getElementById("demo8");

output.innerHTML = slider.value;
output1.innerHTML = slider1.value;
output2.innerHTML = slider2.value;
output3.innerHTML = slider3.value;
output4.innerHTML = slider4.value;
output5.innerHTML = slider5.value;
output6.innerHTML = slider6.value;
output7.innerHTML = slider7.value;
output8.innerHTML = slider8.value;

slider.oninput = function() {
  output.innerHTML = this.value;
}
slider1.oninput = function() {
  output1.innerHTML = this.value;
}

slider2.oninput = function() {
  output2.innerHTML = this.value;
}

slider3.oninput = function () {
  output3.innerHTML = this.value;
}

slider4.oninput = function() {
  output4.innerHTML = this.value;
}

slider5.oninput = function() {
  output5.innerHTML = this.value;
}

slider6.oninput = function () {
  output6.innerHTML = this.value;
}

slider7.oninput = function() {
  output7.innerHTML = this.value;
}

slider8.oninput = function() {
  output8.innerHTML = this.value;
}