function getMiddle(s){
  
  if (s.length % 2 === 0){
    return s.slice(s.length/2 -1, s.length/2 + 1) // this slice returns the two middle elements IF it is an even number 
    
  } else {
    return s.slice(s.length/2, s.length/2 +1) // this slice returns a string with just the middle element since it does not reach the end
  }
};
