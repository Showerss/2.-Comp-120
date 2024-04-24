'''
basically recurion but with specific applications
    recursion is one thing, over and over, working towards one base casea

recursive backtracking -
    is many potential solutions 
    base case is one potential solution, itll create trees worth of solutions
    initial call begins with an empty solution 

    one potential pattern: choice -> explore -> unchoose
        if that potential choice makes a base case return true
    
    used for 3 types of problems
        1. generate all possible solutions
            two recursive calls (like fibonacchi)
                - has an option
                - doesnt include that option 
        
        2. make sure there exists at least one solution
            make a choice 
            explore that choice recursively 
            if good, then good ... if unsuccessful, then unchoose

        3. find a best possible solution


    youll track options to consider and choices made (which starts empty)

    

'''



# Exercise 1:
"""
    Write recursive function that prints out all possible permutations
    of a given string
"""
def word_scramble(options: str, so_far: str):
    """ Prints all permutations of <options>,
      with <so_far> as a prefix."""
    if len(options) == 0:
        print(so_far)
    else:
        for i in range(len(options)): #for each letter left in options
            choice = options[i] #itll choose 0,1,2,3, etc with each new loop
            remaining = options[:i] + options[i+1:] #
            word_scramble(remaining, so_far + choice)

word_scramble("cat", "")

# Exercise 2:
"""
    Write a recursive function that identifies whether or not you
    can remove a single letter at a time and still be a valid word
    after each removal
    Ex: Input: "cart"
        Solution: Yes! ("cart" 🡪 "art" 🡪 "at" 🡪 "a")
    Input: "rope"
        Solution: No!
"""
def shrinkable(word: str, valid_words: list[str]) -> bool: #since this returns a bool the returns are just true/false
    """ Returns True if word is shrinkable. """

    if word not in valid_words:
        return False
    elif len(word) == 1:
        return True
    
    else:
        for i in range(len(word)):
            next_word = word[:i] + word[i+1:]
            if shrinkable(next_word, valid_words):
                return True
            # if next_word in valid_words:
            #     return True
        return False
    
print("cart", shrinkable("cart", ["cart", "art", "cat", "a", "car", "at"]))
print("rope", shrinkable("rope", []))

# Exercise 3:
"""
    Write a recursive function that when given a list of items,
    all the possible subsets of those items are printed.
"""
def possible_subsets(items: list, subset_so_far: set) -> None:
    """
    returns true if 
    """
    if len(items) == 0:
        if len(subset_so_far) > 0:
            print(subset_so_far)
        return #since its return None we only need a return initiially 
    else:
        #case1: include the superhero
        subset_so_far.add(items[0])
        possible_subsets(items[1:], subset_so_far)
        #always take first item of the list take from index 1 to the end

        #case2: dont include superhero
        subset_so_far.remove(items[0])
        possible_subsets(items[1:], subset_so_far)
        #take the first item of the list and add it to the subset so far

        #since it returns none then we dont need any return statement here
    
possible_subsets(["Iron Man", "Captain Marvel"], set())