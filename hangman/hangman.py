from category import categoryAnimals
from category import categorySports
from category import categoryFruits
from random import randint

def hangman():
    select = "y"
    while(select == "y"):
        showCategory()

        categoryInput = input("Category >> ")
        print()

        checkInput(categoryInput)

def checkInput(categoryInput):
    CONST_MIN_CATEGORY = 0
    CONST_MAX_CATEGORY = 3
    try:
        categoryInput = int(categoryInput)
        play(categoryInput) if (CONST_MIN_CATEGORY < categoryInput <= CONST_MAX_CATEGORY) else print("\t\tError : Please input 1-3.\n")
    except ValueError:
        print("\t\tError : Please input 1-3.\n")

def showCategory():
    print("Select Category (Input 1-3)")
    print("1 : Animals")
    print("2 : Sports")
    print("3 : Fruits")

def prepare(rand, categoryInput):
    if (categoryInput == 1):
        print("Hint : \"" + categoryAnimals.getHint(rand) + "\"")
        return categoryAnimals.getAnswer(rand)
    elif (categoryInput == 2):
        print("Hint : \"" + categorySports.getHint(rand) + "\"")
        return categorySports.getAnswer(rand)
    else:
        print("Hint : \"" + categoryFruits.getHint(rand) + "\"")
        return categoryFruits.getAnswer(rand)
    print()

def play(categoryInput):
    CONST_MIN_CHOICE = 0
    CONST_MAX_CHOICE = 4
    rand = randint(CONST_MIN_CHOICE, CONST_MAX_CHOICE)
    answer = prepare(rand, categoryInput)
    answerLen = len(answer)
    resultList = createList(answer)
    wrongGuessed = []
    score = 0
    life = 10

    while (("_" in resultList) and life > 0):
        isGuessed = True
        print(" ".join(resultList), "\tScore : %d, Remaining wrong guess : %d" % (score, life), end = "")
        
        checkEmptyList(wrongGuessed)

        character = input("Guess the character >> ").lower()
        print()

        if (isCharacter(character)):
            for i in range (len(answer)):
                if ((character in resultList) and isGuessed):
                    print("\t\t\"" + character + "\"" + " already guessed.")
                    print()
                    life -= 1
                    score -= 10 if (score - 10 >= 0) else 0
                    isGuessed = False
                    break
                elif (character == answer[i]):
                    resultList[i] = character
                    score += 10
                    isGuessed = False

            if(isGuessed):
                life -= 1
                score -= 10 if (score - 10 >= 0) else 0
                addGuessedToList(character, wrongGuessed)

    else:
        checkWinOrLose(life, answer, score)
        
def isCharacter(character):
    if (len(character) == 1):
        if (character.isalpha()):
            return True
        else:
            print("\t\tError : Don't input digit.\n")
            return False
    else:
        print("\t\tError : Please input a character.\n")
        return False

def createList(text):
    resultList = []
    for i in text:
        resultList.append("_")
    return resultList

def checkEmptyList(wrongGuessed):
    if(len(wrongGuessed) != 0):
        print(", Wrong guessed : " + " ".join(wrongGuessed))
    else:
        print()

def addGuessedToList(character, wrongGuessed):
    if character not in wrongGuessed:
        wrongGuessed.append(character)

def checkWinOrLose(life, answer, score):
    if (life > 0):
        print("PROOF! Your score is : %d" % score)
        print("The answer is : " + answer)
    else:
        print("Game Over.")

    select = input("Continue play? (Press y to continue | Press anything to exit) >> ")
    if (select != "y"):
        exit()
    
    print("\n\t\t" + "---------- " + "New Game" + " ----------\n")

hangman()