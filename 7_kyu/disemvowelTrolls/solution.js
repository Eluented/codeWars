function disemvowel(str) {
  return str.replace(/[aeiou]/gi, ''); // googled how to remove vowels from a string which returned a regrex expression with .replace method - checked it out and tried to learn from it - looks the string and replaces it with an empty string
};
