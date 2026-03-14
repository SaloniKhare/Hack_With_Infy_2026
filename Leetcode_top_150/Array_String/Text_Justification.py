# ======================================================
# TEXT JUSTIFICATION - ALL APPROACHES
# ======================================================

# Problem (LeetCode 68):
# Given an array of words and a maxWidth,
# format the text so that each line has exactly maxWidth characters
# and is fully justified.


# ------------------------------------------------------
# 1️⃣ Greedy Line Building (Standard Interview Solution) ⭐
# ------------------------------------------------------

class GreedySolution:
    def fullJustify(self, words, maxWidth):

        res = []
        i = 0

        while i < len(words):

            line = []
            length = 0

            # collect words for the current line
            while i < len(words) and length + len(words[i]) + len(line) <= maxWidth:
                line.append(words[i])
                length += len(words[i])
                i += 1

            spaces = maxWidth - length
            gaps = len(line) - 1

            # last line or single word → left justified
            if i == len(words) or gaps == 0:
                line_str = " ".join(line)
                line_str += " " * (maxWidth - len(line_str))
                res.append(line_str)

            else:
                even_space = spaces // gaps
                extra_space = spaces % gaps

                line_str = ""

                for j in range(gaps):
                    line_str += line[j]
                    line_str += " " * (even_space + (1 if j < extra_space else 0))

                line_str += line[-1]
                res.append(line_str)

        return res


# ------------------------------------------------------
# 2️⃣ Manual Space Distribution
# ------------------------------------------------------

class ManualDistributionSolution:
    def fullJustify(self, words, maxWidth):

        result = []
        i = 0

        while i < len(words):

            start = i
            total_len = len(words[i])
            i += 1

            while i < len(words) and total_len + len(words[i]) + (i - start) <= maxWidth:
                total_len += len(words[i])
                i += 1

            gaps = i - start - 1
            line = ""

            if i == len(words) or gaps == 0:

                for j in range(start, i):
                    line += words[j] + " "

                line = line[:-1]
                line += " " * (maxWidth - len(line))

            else:

                spaces = (maxWidth - total_len) // gaps
                extra = (maxWidth - total_len) % gaps

                for j in range(start, i - 1):
                    line += words[j]
                    line += " " * (spaces + (1 if extra > 0 else 0))
                    extra -= 1

                line += words[i - 1]

            result.append(line)

        return result


# ------------------------------------------------------
# 3️⃣ Pythonic Approach
# ------------------------------------------------------

class PythonicSolution:
    def fullJustify(self, words, maxWidth):

        res = []
        line = []
        length = 0

        for word in words:

            if length + len(word) + len(line) > maxWidth:

                for i in range(maxWidth - length):
                    line[i % (len(line)-1 or 1)] += " "

                res.append("".join(line))
                line = []
                length = 0

            line.append(word)
            length += len(word)

        last = " ".join(line)
        last += " " * (maxWidth - len(last))
        res.append(last)

        return res
