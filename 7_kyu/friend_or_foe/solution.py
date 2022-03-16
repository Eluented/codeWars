def friend(x):
  new_friends = []

  for friend in x:

    if (len(friend) == 4): # tests if the length of the friend is 4 letters long
      new_friends.append(friend) # appends the 4 letter name friend to the new_friends list
            
  return new_friends
