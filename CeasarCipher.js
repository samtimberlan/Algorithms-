function rot13(str) {
  // LBH QVQ VG!
  const alphabets = {
    A: "N",
    B: "O",
    C: "P",
    D: "Q",
    E: "R",
    F: "S",
    G: "T",
    H: "U",
    I: "V",
    J: "W",
    K: "X",
    L: "Y",
    M: "Z",
    N: "A",
    O: "B",
    P: "C",
    Q: "D",
    R: "E",
    S: "F",
    T: "G",
    U: "H",
    V: "I",
    W: "J",
    X: "K",
    Y: "L",
    Z: "M"
  };

  var result = [];
  str
    .toUpperCase()
    .split("")
    .map(character => {
      result.push(convert(character));
      if (!convert(character)) {
        result.push(character);
      }
    });

  function convert(character) {
    for (var key in alphabets) {
      if (key === character) {
        return alphabets[key];
      }
    }
  }

  str = result.join("");
  console.log(str);
  return str;
}

rot13("Why did the chicken cross the road?"); // JUL QVQ GUR PUVPXRA PEBFF GUR EBNQ?
rot13("GUR DHVPX OEBJA SBK WHZCF BIRE GUR YNML QBT"); // THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG
