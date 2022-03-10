function reverseLetter(str) {
  let reversed = ""
  
  for (let i = str.length -1; i >= 0; i--){ // went in a reversed for loop 
    
    if ((/[a-zA-Z]/).test(str[i])){ // used regrex to test if the character is an alphabetical character
      reversed += str[i]
      
    } else {
        continue; // skip to the next iteration if non-alphabetical
      }
  }
  return reversed;
};
