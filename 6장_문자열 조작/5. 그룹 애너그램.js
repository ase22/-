const arr = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat'];
const arr2= arr.map(word => word.split('').sort((a, b) => a.charCodeAt(0) - b.charCodeAt(0)).join(''));
const obj = {};

for (let i = 0; i < arr.length; i++) {
  const sortedString = arr[i].split('').sort((a, b) => a.charCodeAt(0) - b.charCodeAt(0)).join('');
  
  if (!(Object.keys(obj).includes(sortedString))) {
    obj[sortedString] = [arr[i]];
  } else {
    obj[sortedString].push(arr[i]);
  }
}

const arr3 = [];

for (let i = 0; i < Object.values(obj).length; i++) {
  arr3.push(Object.values(obj)[i]);
}

console.log(arr3);
