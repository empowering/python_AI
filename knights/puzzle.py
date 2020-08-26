from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
sentence = And(AKnight, AKnave)
knowledge0 = And(

    # Each person should be 
    # either a Knight or a Knave, not both.
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),

    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),

    Or(CKnave, CKnight),
    Not(And(CKnave, CKnight)),

    # Sentence is true
    # only if A is a knight 
    Implication(AKnight, sentence)

    # Implication(AKnave, Or(BKnight, CKnight)),

    # Biconditional(AKnight, sentence)
    # Biconditional(AKnave, Not(sentence))

)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
sentence = And(AKnave, BKnave)
knowledge1 = And(

    # Each person should be 
    # either a Knight or a Knave, not both.
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),

    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),

    Or(CKnave, CKnight),
    Not(And(CKnave, CKnight)),

    # Only one Knight exists
    # Or(AKnight, BKnight, CKnight),
    # Implication(AKnight, And(BKnave, CKnave)),
    # Implication(BKnight, And(AKnave, CKnave)),
    # Implication(CKnight, And(AKnave, BKnave)),

    # Sentence is true
    # only if A is a knight 
    Biconditional(AKnight, sentence)

)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
sentenceA = Or(And(AKnight,BKnight),And(AKnave,BKnave))
sentenceB = Or(And(AKnight,BKnave),And(AKnave,BKnight))

knowledge2 = And(
    
    # Each person should be 
    # either a Knight or a Knave, not both.
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),

    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),

    Or(CKnave, CKnight),
    Not(And(CKnave, CKnight)),

    # Sentence is true
    # only if the speaker says True
    And(
        Biconditional(AKnight, sentenceA),
        Biconditional(BKnight, sentenceB)
    )

)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."

# A said B is * == Biconditional(AKnight, B*)
# Since this statement is true if and only if A is a knight 
sentenceA = Biconditional(AKnight, Not(AKnave))
sentenceB = And(Biconditional(BKnight, Biconditional(AKnight, AKnave)), CKnave)
sentenceC = AKnight

knowledge3 = And(

    # Each person should be 
    # either a Knight or a Knave, not both.
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),

    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),

    Or(CKnave, CKnight),
    Not(And(CKnave, CKnight)),

    ## THIS CONDITION WAS NOT GIVEN ! 
    # # Only one Knight exists
    # Implication(AKnight, And(BKnave, CKnave)),
    # Implication(BKnight, And(AKnave, CKnave)),
    # Implication(CKnight, And(AKnave, BKnave)),

    # Sentence is true
    # only if the speaker says True
    And(
        Biconditional(AKnight, sentenceA),
        Biconditional(BKnight, sentenceB),
        Biconditional(CKnight, sentenceC)
    )

)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
