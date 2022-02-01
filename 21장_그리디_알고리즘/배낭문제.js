const cargo = [
  [4, 12],
  [2, 1],
  [10, 4],
  [1, 1],
  [2, 2]
];

const capacity = 15;

function fillinBackpack(cargo, capacity) {
  let backpackCapacity = capacity;
  let money = 0;

  const pack = cargo.map(item => [item[0] / item[1], item[0], item[1]]).sort((a, b) => b[0] - a[0]);

  for (const item of pack) {
    if ((backpackCapacity - item[2]) >= 0) {
      backpackCapacity -= item[2];
      money += item[1];
    }
    else {
      const remainingWeightProportion = backpackCapacity / item[2];
      backpackCapacity = 0;
      money += remainingWeightProportion * item[0];
    }
  }

  return money;
}

console.log(fillinBackpack(cargo, capacity));