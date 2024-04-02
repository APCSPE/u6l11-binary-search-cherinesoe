import math

def binary_search(my_list, target):
    lower_idx = 0
    upper_idx = len(my_list) - 1
    comparisons = 0  # track number of comparisons

    while lower_idx <= upper_idx:
        comparisons = comparisons + 1
        
        mid_idx = math.ceil((lower_idx + upper_idx) / 2) # calculate middle index; ceil function rounds up

        # compare target with value at the middle index
        if my_list[mid_idx] < target:
            print("index " + str(mid_idx) + ": value = " + str(my_list[mid_idx]) + " --> too low!")
            upper_idx = mid_idx - 1 # update lower index
        elif my_list[mid_idx] > target:
            print("index " + str(mid_idx) + ": value = " + str(my_list[mid_idx]) + " --> too high!")
            lower_idx = mid_idx + 1 # update upper index
        else:
            print("index " + str(mid_idx) + ": value = " + str(my_list[mid_idx]) + " --> FOUND!")
            print("number of comparisons: " + str(comparisons))
            return True # target is found, early return true
    
    print("target not in list")
    print("number of comparisons: " + str(comparisons))
    return False # loop ended without returning true, so target not in list


# MAIN PROGRAM
words = ["apple", "big", "carrot", "cram", "dear", "dingo", "dire", "elephant", "ellipse", "frank", "fun", "ginger", "grade", "graduate", "ice cream", "icky", "jingle", "juggle", "kangaroo", "kazoo", "kite", "koala", "lion", "lone", "magic", "mango", "mississippi", "mystify", "need", "nod", "nun", "oh", "omen", "paper", "pepper", "peppy", "popper", "poppy", "puppy", "quit", "quit", "rail", "ring", "roll", "saucy", "tame", "taunt", "violin", "waiter", "water", "yaaas!", "zebra", "zzz"]



# write your test code:
print(binary_search(words, "fun"))
print(binary_search(words, "water"))
print(binary_search(words, "mississippi"))
print(binary_search(words, "queen"))
