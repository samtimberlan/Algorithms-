function diffArray(arr1, arr2) {
  var newArr = [];
  arr1.filter(el => {
    if (!arr2.includes(el)) {
      newArr.push(el);
    }
  });
  arr2.filter(el => {
    if (!arr1.includes(el)) {
      newArr.push(el);
    }
  });
  // Same, same; but different.
  console.log(newArr.map(el => el));
  return newArr;
}

function diffArrayAdvFCC(arr1, arr2) {
  var newArr = [...diff(arr1, arr2), ...diff(arr2, arr1)];

  //reusable function to filter diff
  function diff(arr1, arr2) {
    return arr1.filter(el => arr2.indexOf(el) === -1);
  }
  // Same, same; but different.
  console.log(newArr.map(el => el));
  return newArr;
}

diffArray([1, 2, 3, 5, 7], [1, 2, 3, 4, 5]);
diffArrayAdvFCC([1, 2, 3, 5, 7], [1, 2, 3, 4, 5]);
