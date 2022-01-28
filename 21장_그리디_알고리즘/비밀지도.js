const n = 5;
const arr1 = [9, 20, 28, 18, 11];
const arr2 = [30, 1, 21, 17, 28];

function solution(n, arr1, arr2) {
  const answer = [];

  function getMap(n, arr) {
    const map = arr.map(number => {
      let binaryNumber = number.toString(2);
      let count = binaryNumber.length;

      while (count < n) {
        binaryNumber = '0' + binaryNumber;
        count++;
      }

      return binaryNumber;
    });

    return map;
  }

  const map1 = getMap(n, arr1);
  const map2 = getMap(n, arr2);

  for (let i = 0; i < map1.length; i++) {
    code = '';

    for (let j = 0; j < map1.length; j++) {
      if (map1[i][j] === '1' || map2[i][j] === '1') {
        code += '#';
      } else {
        code += ' ';
      }
    }

    answer.push(code);
  }

  return answer;
}
