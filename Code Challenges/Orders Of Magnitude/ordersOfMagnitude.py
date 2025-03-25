def ordersOfMagnitude(text_input: str) -> int:
    magnitudes = {'hundred':100, 'thousand':1_000, 'million':1_000_000}
    num, magnitude = text_input.split()
    num = float(num)
    magnitude = magnitudes[magnitude]
    return(int(num * magnitude))

if __name__ == "__main__":
    answer = ordersOfMagnitude(input("Enter a number with a magnitude (ex. 3.2 thousand): "))
    print(answer)
