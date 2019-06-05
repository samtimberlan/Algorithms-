//Number Swapper: Write a function to swap a number in place (that is, without temporary vari­ ables).
function swapInPlace(num1, num2) {
  num1 = num2 - num1; // expendable diff
  num2 = num2 - num1;
  num1 = num1 + num2;
  console.log(num1, num2);
  return num1, num2;
}

swapInPlace(87, 45);
swapInPlace(287, 945);
swapInPlace(0, 45);
