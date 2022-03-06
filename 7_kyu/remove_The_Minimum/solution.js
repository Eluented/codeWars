function removeSmallest(numbers) {
  let lowest = numbers[0] // can also use an object here to specify the lowest number AND the index if you want instead of using indexOf()
  for (let i = 0; i < numbers.length; i++){
    if (numbers[i] < lowest){
      lowest = numbers[i]
    } 
  } 
  let indexOfNum = numbers.indexOf(lowest)
  return numbers.slice(0, indexOfNum).concat(numbers.slice(indexOfNum+1))
}
