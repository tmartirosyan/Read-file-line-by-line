def readFileLines(path: str) -> list:
    with open(path, "r") as text:
        return text.readlines()


path = input("Write your text file path : ")
print(readFileLines(path))