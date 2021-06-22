#Code to convert american number to word
ones = {
    0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
    7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',
    13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
    17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
tens = {
    2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty',
    7: 'seventy', 8: 'eighty', 9: 'ninety'}
illions = {
    1: 'thousand', 2: 'million', 3: 'billion', 4: 'trillion', 5: 'quadrillion',
    6: 'quintillion', 7: 'sextillion', 8: 'septillion', 9: 'octillion',
    10: 'nonillion', 11: 'decillion'}

def numToWord(n):
    try:
        if n == 0:
            return 'zero'
        return getNumberPos(n)
    except Exception:
        print(str(Exception))

def getNumberPos(n):
    if n < 20:
        return ones[n]
    if n < 100:
        return merge(tens[n//10], ones[n%10])
    if n < 1000:
        return divide(n, 100, 'hundred')
    for illions_number, illions_name in illions.items():
        if n < 1000**(illions_number + 1):
            break
    return divide(n, 1000**illions_number, illions_name)


def divide(dividend, divisor, magnitude):
    return merge(
        getNumberPos(dividend // divisor),
        magnitude,
        getNumberPos(dividend % divisor),
    )

def merge(*args):
    return ' '.join(filter(bool, args))
    
while True:
    n=int(input("Enter number between[0 to decillion]:"))
    if n<0 or n>(10**33):
        print("Please enter valid number")
        continue
    else:
        print(numToWord(n))
        break

"""
#By using bultin method
import inflect
p = inflect.engine()
print(p.number_to_words(99))
print(p.number_to_words(100000))
"""