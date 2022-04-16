
import string
import random

class PwdGenerator:
    def __init__(self) -> None:
        pass

    def generatePassword(attribs={"length": 16, "upper": 1, "num": 1, "special": 1}):
        pwdLen = attribs["length"]
        minUpper = attribs["upper"]
        minNum = attribs["num"]
        minSpecial = attribs["special"]
        minReq = minUpper + minNum + minSpecial
        rest = pwdLen - minReq

        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        num = string.digits
        special = string.punctuation
        all = lower + upper + num + special

        chosenU = random.sample(upper, minUpper)
        chosenN = random.sample(num, minNum)
        chosenS = random.sample(special, minSpecial)
        chosenR = random.sample(all, rest)

        chosen = "".join(chosenU) + "".join(chosenN) + \
            "".join(chosenS) + "".join(chosenR)

        return "".join(random.sample(chosen, pwdLen))


    # length = input("pwd length: ")
    # upper = input("minimum uppercase: ")
    # numbers = input("minimum numbers: ")
    # special = input("minimum special chars: ")
    # print(generatePassword({"length": int(length), "upper": int(
    #     upper), "num": int(numbers), "special": int(special)}))
