nums = [1, 2, 3]

function practice(nums) {
  const results = []

  const dfs = (index, elements) => {
    results.push(elements)

    for (let i = index; i < nums.length; i++) {
      const newList = JSON.parse(JSON.stringify(elements))
      newList.push(nums[i])
      dfs(i + 1, newList)
    }
  }

  dfs(0, [])

  return results
}

console.log(practice(nums))