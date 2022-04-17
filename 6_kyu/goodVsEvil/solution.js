function goodVsEvil(good, evil){
  // Good Score!
  let goodArrayInt = good.split(" ").map(x => parseInt(x)) // turned the string of numbers into an array of integers
  let goodScore = (goodArrayInt[0] * 1) + (goodArrayInt[1] * 2) + (goodArrayInt[2] * 3) + (goodArrayInt[3] * 3) + (goodArrayInt[4] * 4) + (goodArrayInt[5] * 10) // adding the score up based on the values they gave in the question 
  
  // Evil Score!
  let evilArrayInt = evil.split(" ").map(x => parseInt(x))
  let evilScore = (evilArrayInt[0] * 1) + (evilArrayInt[1] * 2) + (evilArrayInt[2] * 2) + (evilArrayInt[3] * 2) + (evilArrayInt[4] * 3) + (evilArrayInt[5] * 5) + (evilArrayInt[6] * 10) // adding the evil score based on the given values
  
  // Comparing Each Score!
  if (goodScore > evilScore) {
    return "Battle Result: Good triumphs over Evil"
  } else if (evilScore > goodScore) {
    return "Battle Result: Evil eradicates all trace of Good"
  } else {
    return "Battle Result: No victor on this battle field"
  }
}
