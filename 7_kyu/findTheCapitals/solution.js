var capitals = function (word) {
  indexOfCapitals = []
	for (let i=0; i < word.length; i++){
    if (word[i] === word[i].toUpperCase()){ // checks if the current letter is a capital or not
      indexOfCapitals.push(word.indexOf(word[i])) 
    }
  }
  return indexOfCapitals;
};
