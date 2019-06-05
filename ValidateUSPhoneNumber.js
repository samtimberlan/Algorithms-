//Tests
//true
telephoneCheck("1 (555) 555-5555");
telephoneCheck("1 555-555-5555");
telephoneCheck("1(555)555-5555");
telephoneCheck("555-555-5555");
telephoneCheck("(555)-555-5555");
telephoneCheck("1 (555) 555-5555");
telephoneCheck("1 555-555-5555");
telephoneCheck("1(555)555-5555");
telephoneCheck("555-555-5555");
telephoneCheck("(555)-555-5555");

//false
telephoneCheck("2 (757) 622-7382");
telephoneCheck("(555-555-5555");
telephoneCheck("-1 (757) 622-7382");
telephoneCheck("2 757 622-7382");
telephoneCheck("2(757)622-7382");
telephoneCheck("(6054756961)");
telephoneCheck("123**&!!asdf#");
telephoneCheck("1 555)555-5555");
telephoneCheck("1 555)555-5555");
telephoneCheck("555)-555-5555");

function telephoneCheck(str) {
  // Good luck!
  var regexNumOnly = /(^\d{3}(\s|-|)\d{3}(\s|-|)\d{4}$)/g;
  var regexNumParen = /(^(\()\d{3}(\)){1})(\s|-|)\d{3}-\d{4}/g; //not handling second parenthesis at first match
  var regexCountryCode = /^(1(\s?-?))(\d{3}(\s?-?)\d{3}(\s|-)\d{4})/g;
  var regexCountryCodeParen = /^(1(\s?-?))((\()\d{3}(\))(\s?-?)\d{3}(\s|-)\d{4})/g;

  if (
    regexNumOnly.test(str) ||
    regexNumParen.test(str) ||
    regexCountryCode.test(str) ||
    regexCountryCodeParen.test(str)
  ) {
    var flag = true;
    console.log(flag);
    return flag;
  }
  flag = false;
  console.log(flag);
  return false;
}

//---Second regex. Does not validate one sided parenthesis like 1 555)555-5555"
// function telephoneCheck(str) {
//   // Good luck!
//   var regexNumOnly = /(^(1?(\s|-)?)(\(?)\d{3}(\s?-?)(\)?)(\s?-?)\d{3}(\s?-?)\d{4}$)/g;

//   return regexNumOnly.test(str) ? console.log(true) : console.log(false);
// }
