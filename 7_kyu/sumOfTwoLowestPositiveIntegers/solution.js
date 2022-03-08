function sumTwoSmallestNumbers(numbers) {  
  let descending = numbers.sort((a,b)=> a-b) // doing a compare function so the numbers are sorted from lowest to highest
  return descending[0] + descending[1];
};
