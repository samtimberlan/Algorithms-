var RomanNumerals = [
  ["I", "IV", "V", "IX"],
  ["X", "XL", "L", "XC"],
  ["C", "CD", "D", "CM"],
  ["M"]
];
var romanNumResultArr = [];

function convertToRoman(num) {
  if (num >= 4000) {
    return "Unfortunately, numbers from 4000 and above do not have roman numerals";
  }

  var givenNumeral = num
    .toString()
    .split("")
    .map(Number);

  for (var i = givenNumeral.length; i > 0; i--) {
    convertToRomanUnit(givenNumeral.shift(), RomanNumerals[i - 1]);
  }

  var result = romanNumResultArr.join("");
    console.log(result)
  return result;
}

function convertToRomanUnit(num, romArr) {
  var arrayToBeUsed = romArr;
  if (num <= 3) {
    while (num > 0) {
      romanNumResultArr.push(arrayToBeUsed[0]);
      num--;
    }
  }
  if (num == 4) {
    romanNumResultArr.push(arrayToBeUsed[1]);
  }

  if (num >= 5 && num < 9) {
    romanNumResultArr.push(arrayToBeUsed[2]);
    while (num - 5 > 0) {
      romanNumResultArr.push(arrayToBeUsed[0]);
      num--;
    }
  }

  if (num == 9) {
    romanNumResultArr.push(arrayToBeUsed[3]);
  }
}

convertToRoman(891);
//--- Second Algorithm---

// var convertToRoman = function(num) {

//     var decimalValue = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ];
//     var romanNumeral = [ 'M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I' ];

//     var romanized = '';

//     for (var index = 0; index < decimalValue.length; index++) {
//       while (decimalValue[index] <= num) {
//         romanized += romanNumeral[index];
//         num -= decimalValue[index];
//       }
//     }

//     return romanized;
//   }

// test here
//convertToRoman(36);

convertToRoman(3000);
