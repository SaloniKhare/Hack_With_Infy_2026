# ======================================================
# INTEGER TO ROMAN - ALL APPROACHES
# ======================================================

# Problem (LeetCode 12):
# Convert an integer to a Roman numeral.

# Roman symbols:
# I=1, V=5, X=10, L=50
# C=100, D=500, M=1000

# Special numbers:
# 4 = IV
# 9 = IX
# 40 = XL
# 90 = XC
# 400 = CD
# 900 = CM


# ------------------------------------------------------
# 1️⃣ Brute Force (Repeated Subtraction)
# ------------------------------------------------------

class BruteForceSolution:
    def intToRoman(self, num: int) -> str:

        values = [
            (1000,"M"), (900,"CM"), (500,"D"), (400,"CD"),
            (100,"C"), (90,"XC"), (50,"L"), (40,"XL"),
            (10,"X"), (9,"IX"), (5,"V"), (4,"IV"), (1,"I")
        ]

        result = ""

        for value, symbol in values:
            while num >= value:
                result += symbol
                num -= value

        return result


# ------------------------------------------------------
# 2️⃣ Greedy (Most Common Interview Solution) ⭐
# ------------------------------------------------------

class GreedySolution:
    def intToRoman(self, num: int) -> str:

        values = [
            1000,900,500,400,
            100,90,50,40,
            10,9,5,4,1
        ]

        symbols = [
            "M","CM","D","CD",
            "C","XC","L","XL",
            "X","IX","V","IV","I"
        ]

        result = ""

        for i in range(len(values)):
            count = num // values[i]
            result += symbols[i] * count
            num %= values[i]

        return result


# ------------------------------------------------------
# 3️⃣ Dictionary Mapping (Digit Based)
# ------------------------------------------------------

class DigitMappingSolution:
    def intToRoman(self, num: int) -> str:

        thousands = ["", "M", "MM", "MMM"]
        hundreds  = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        tens      = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        ones      = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

        return (
            thousands[num // 1000] +
            hundreds[(num % 1000) // 100] +
            tens[(num % 100) // 10] +
            ones[num % 10]
        )


# ------------------------------------------------------
# 4️⃣ Stack-like Construction
# ------------------------------------------------------

class StackStyleSolution:
    def intToRoman(self, num: int):

        mapping = [
            (1000,"M"), (900,"CM"), (500,"D"), (400,"CD"),
            (100,"C"), (90,"XC"), (50,"L"), (40,"XL"),
            (10,"X"), (9,"IX"), (5,"V"), (4,"IV"), (1,"I")
        ]

        result = []
        i = 0

        while num > 0:

            value, symbol = mapping[i]

            if num >= value:
                result.append(symbol)
                num -= value
            else:
                i += 1

        return "".join(result)


# ------------------------------------------------------
# 5️⃣ Recursive Approach
# ------------------------------------------------------

class RecursiveSolution:

    mapping = [
        (1000,"M"), (900,"CM"), (500,"D"), (400,"CD"),
        (100,"C"), (90,"XC"), (50,"L"), (40,"XL"),
        (10,"X"), (9,"IX"), (5,"V"), (4,"IV"), (1,"I")
    ]

    def intToRoman(self, num: int):

        for value, symbol in self.mapping:
            if num >= value:
                return symbol + self.intToRoman(num - value)

        return ""
