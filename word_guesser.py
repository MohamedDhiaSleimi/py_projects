import random

word_list = ["materialistic","jewel","typical","tail","tranquil","beef","gun","brief","machine","entertaining","spiritual","miss","government","flippant","silly","soothe","town","brave","bear","tight","available","laugh","pathetic","cool","ignore","deep","vigorous","tidy","heap","nice","cream","respect", "improve","amazing","tickle","salt","toys","foot","mourn","agreement","left","far-flung","exciting","poor","complete","challenge","discreet","rhyme","wire","aftermath","board","blink","abject","craven","bite","juvenile","gruesome","stupendous","gentle","giant","mountain","historical","blood","strip","fascinated","silk","colour","dislike", "amusement","petite","wrap","bushes","ethereal","lively","handle","please","tie","wander","trite","pop","nonchalant","graceful","selfish","umbrella","detect","unwritten","husky","remember","clover","verse","male","white","poison","owe","old","telephone","hushed","loud","oil","applaud"]

rand_word = random.choice(word_list)

guesses_left = len(rand_word)
guesses = ""
while guesses_left > 0:
    wrong = 0
    for char in rand_word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_")
            wrong += 1
    if wrong == 0:
        print("You Win")
        print("The word is: ", word)
        break
    print()
    guess = input("guess a character:")
    guesses += guess
    if guess not in rand_word:
        guesses_left -= 1
        print("Wrong")
        print("You have", + guesses_left, 'more guesses')
        if guesses_left == 0:
            print("You Loose")
            print(" the word is ",rand_word)