"""reducible.py"""
# Name 1: Swati Misra
# EID 1: SM83264

# Name 2: Sanjitha Venkata
# EID 2: sv28325

import sys


# Input: takes as input a positive integer n
# Output: returns True if n is prime and False otherwise
def is_prime(n):
    """is prime"""
    if n == 1:
        return False

    limit = int(n ** 0.5) + 1
    div = 2
    while div < limit:
        if n % div == 0:
            return False
        div += 1
    return True



# Input: takes as input a string in lower case and the size
#        of the hash table
# Output: returns the index the string will hash into
def hash_word(s, size):
    """hash word"""
    hash_idx = 0
    len_s = len(s)
    for j in range(len_s):
        letter = ord(s[j]) - 96
        hash_idx = (hash_idx * 26 + letter) % size
    return hash_idx



# Input: takes as input a string in lower case and the constant
#        for double hashing
# Output: returns the step size for that string
def step_size(s, const):
    """step size"""
    return const-(hash_word(s,const)) # %const




# Input: takes as input a string and a hash table
# Output: no output; the function enters the string in the hash table,
#         it resolves collisions by double hashing
def insert_word(s, hash_table):
    """insert word"""
    # const = hash_table.size()-1
    # while is_prime(const) is False:
    #     const -= 1


    index = hash_word(s, len(hash_table))
    if hash_table[index] is None:
        hash_table[index] = s
    elif hash_table[index] == s:
        pass
    else:
        while hash_table[index] != "" and hash_table[index]!=s:
            index=(index+step_size(s,3))%len(hash_table)
        hash_table[index]=s




# Input: takes as input a string and a hash table
# Output: returns True if the string is in the hash table
#         and False otherwise
def find_word(s, hash_table):
    """find word"""
    index = hash_word(s, len(hash_table))
    #print("index", index) ##
    while index < len(hash_table):
        if hash_table[index] == "":
            return False
        if hash_table[index] == s:
            return True
        index += step_size(s, 3)
    return False
    #print("hash memo", hash_memo) ##


# Input: string s, a hash table, and a hash_memo
#        recursively finds if the string is reducible
# Output: if the string is reducible it enters it into the hash memo
#         and returns True and False otherwise
def is_reducible(s, hash_table, hash_memo):
    """is reducible"""
    if find_word(s, hash_memo):
        return True
    vowels = ["a", "o", "i"]
    if s in vowels:
        insert_word(s, hash_memo)
        return True
    if find_word(s, hash_table):
        for i in range(len(s)):
            s2 = s[:i] + s[i+1:]
            if is_reducible(s2, hash_table, hash_memo):
                insert_word(s, hash_memo)
                return True
    return False




# Input: string_list a list of words
# Output: returns a list of words that have the maximum length
def get_longest_words(string_list):




    """get longest words"""
    longest_word_list=[]
    max_len=0
    for word in string_list:
        # if len(word)>max_len:
        #     max_len=len(word)
        max_len = max(max_len, len(word))
    for word in string_list:
        if len(word) == max_len:
            longest_word_list.append(word)








    return longest_word_list
















def main():
    """main"""
    # create an empty word_list
    word_list = []








    # read words from words.txt and append to word_list
    # This is an alternative way to input()
    # since sys.stdin is standard input, and standard input
    # can be treated like a file.
    # Recall that standard input is just your terminal,
    # or whatever file you use input redirection with
    for line in sys.stdin:
        line = line.strip()
        word_list.append(line)








    # find length of word_list
    len_word_list = len(word_list)








    # determine prime number N that is greater than twice
    # the length of the word_list
    twice_len = (2 * len_word_list) + 1
    while is_prime(twice_len) is False:
        twice_len += 1








    # create an empty hash_list
    hash_list= []
    #what is a hash list








    # populate the hash_list with N blank strings
    hash_list= [""] * twice_len
    hash_list.append("i")
    hash_list.append("a")
    hash_list.append("o")


    # hash each word in word_list into hash_list
    # for collisions use double hashing








    for i in range(len_word_list):
        insert_word(word_list[i], hash_list)
















    # create an empty hash_memo of size M
    m = int(0.2*len(word_list)+1)








    # we do not know a priori how many words will be reducible
    # let us assume it is 10 percent (fairly safe) of the words
    # then M is a prime number that is slightly greater than
    # 0.2 * size of word_list








    # populate the hash_memo with M blank strings
    hash_memo = [""] * m
    # hash_memo.append("a")
    # hash_memo.append("i")
    # hash_memo.append("o")








    # create an empty list reducible_words
    reducible_words=[]




    #TEST
    #print(is_reducible("in", hash_list, hash_memo))








    #    # for each word in the word_list recursively determine
    #    # if it is reducible, if it is, add it to reducible_words
    #    # as you recursively remove one letter at a time check
    #    # first if the sub-word exists in the hash_memo. if it does
    #    # then the word is reducible and you do not have to test
    #    # any further. add the word to the hash_memo.








    for word in word_list:
        if is_reducible(word, hash_list, hash_memo):
            reducible_words.append(word)








    # #    # find the largest reducible words in reducible_words
    largest_reducible_words = get_longest_words(reducible_words)








    # #    # print the reducible words in alphabetical order
    # #    # one word per line
    sorted_largest_reducible_words=sorted(largest_reducible_words)
    for word in sorted_largest_reducible_words:
        print(word)








if __name__ == "__main__":
    main()
