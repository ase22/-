const sampleString = 'abccccu';

function biggestPalindrome(myStr) {
  let index = myStr.length - 1;

  while (index >= 0) {
    for (let j = 0; myStr.length >= j + index + 1; j++) {
      const newMyCharList = [];

      for (let i = 0; i <= index; i++) {
        newMyCharList.push(myStr[i + j]);
      }
  
      let count = 0;

      for (let i = 0; i < newMyCharList.length; i++) {
        if (newMyCharList[i] !== newMyCharList[newMyCharList.length - i - 1]) {
          count++;
          break;
        }
      }

      if (!count) {
        return newMyCharList;
      }
    }

    index--;
  }
}

console.log(biggestPalindrome(sampleString));

// class Palindrome:
//   def palindrome(self, myStr: str) -> bool:
//     new_str_list = []

//     for char in myStr:
//       if char.isalnum():
//         new_str_list.append(char.capitalize())

//     index = 0

//     for elem in new_str_list:
//       if elem != new_str_list[len(new_str_list) - index - 1]:
//         return False

//       index = index + 1

//     return True

// 1. sampleString.length 부터 시작해서 length == 1일 때 까지 for문을 돌린다.
// 2. 이 때 각각의 길이 + 해당 문자열의 첫 부분의 인덱스 === sampleString.length 인 경우까지만 수행
// 따라서 for문을 2번 돌려야 하고 첫번째 for문에서는 문자열을 잘라야 하고 두번째 for문에서는 2번을 수행하는데 이때 필요한게 이전에 적었던 팰린드롬 코드이다.
// 문자열 자르는법: 문자열은 그냥 새로 하나 만들고 +로 추가해주면 된다. 
// 다시 생각해보면 일단 첫번째 for문은 문자열의 길이를 감소시켜야 하고 두번째 for문은 인덱스를 증가시키면서 문자열을 자른 후 팰린드롬을 판별해야 한다.
// 처음에는 전체 문자열이 팰린드롬인지 확인해야함. i = 0, i < myStr.length, i++
// 두번째부터는 전체 문자열 길이 - 1만큼 해야하므로 i = 
// 근데 while문으로 하면 편할거같은데 i = myStr.length - 1, while ( i > 0) {i--}
