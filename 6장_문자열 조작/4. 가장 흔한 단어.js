const paragragh = "Bob hit a ball, the hit BALL flew far after it was hit";

function mostFrequentWord(string) {
  let tempString = string.toLowerCase();
  const words = tempString.split(' ');

  const checkWords = {};

  for (let i = 0; i < words.length; i++) {
    if (!(words[i] in Object.keys(checkWords))) {
      checkWords[words[i]] = 1;
    } else {
      checkWords[words[i]]++;
    }

  }

  console.log(checkWords);
}

mostFrequentWord(paragragh);


