function wave(str) {
    waveList = []
    for (let i = 0; i < str.length; i++) {
        if (str[i] === " ") {
            continue; // skips when it is an empty space
        } else {
            waveList.push(str.slice(0, i) + str[i].toUpperCase() + str.slice(i + 1)); // pushes the uppercase letter into the new list including the stuff before and after it
        }
    }
    return waveList
};
