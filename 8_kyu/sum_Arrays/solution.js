const sum = (numbers) => {
  if (numbers.length > 1) {
    var sumOfArray = 0
    for (let i=0; i<numbers.length; i++){
      sumOfArray += numbers[i]
    } 
    return sumOfArray
  } else if(numbers.length === 1){
    return parseInt(numbers) // had to use parseInt otherwise the square bracket appearing fails the test result 
  } else {
    return 0
  }}
