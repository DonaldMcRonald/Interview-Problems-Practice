# Input number
inputNumber = 830475039

stack = []

def store(number):
    ones =  ["", "one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
            "sixteen", "seventeen", "eighteen", "nineteen"]
    tens =  ["", "", "twenty", "thirty", "forty", "fifty", "sixty",
            "seventy", "eighty", "ninety"]
    count = 1
    while number is not 0:
        digit = number % 10
        number = number // 10
        if count is 1:
            one = digit
            stack.append(ones[digit])
        elif count is 2:
            if digit is 1:
                stack.pop()
                stack.append(teens[one])
            else:
                stack.append(tens[digit])
        else:
            stack.append("hundred")
            stack.append(ones[digit])
        count += 1

def numberPrinter(number, place):
    places = ["", "thousand", "million", "billion", "trillion"]
    if number is not 0:
        stack.append(places[place])
        store(int(number % 1000))
        numberPrinter(int(number // 1000), int(place + 1))
    else:
        string = ""
        while stack:
            string += stack.pop() + " "
        print(string)

numberPrinter(inputNumber, 0)
