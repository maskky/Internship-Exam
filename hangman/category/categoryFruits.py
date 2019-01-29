def categoryFruits():
    hintAndValue = {
        "Queen of fruits.", "durian",
        "Red and hairy.", "rambutan",
        "Very sour.", "lime",
        "Monkey.", "banana",
        "Witch's poison", "apple"
    }

def getHint(index):

    hints = ["Queen of fruits.", "Red and hairy.", "Very sour.", "Monkey.", "Witch's poison."]
    return (hints[index])

def getAnswer(index):

    answers = ["durian", "rambutan", "lime", "banana", "apple"]
    return (answers[index])