def find_longest_substring(word1, word2):
    table = [[{"occurrences": 0, "string":""} for __ in word2] for _ in word1]
    biggest_match = {"occurrences": 0, "string":""}

    for i, char1 in enumerate(word1):
        for j, char2 in enumerate(word2):
            if char1 == char2:
                if i == 0 or j == 0:
                    table[i][j]["occurrences"] = 1
                    table[i][j]["string"] = char1
                    continue
                
                previous = table[i-1][j-1]
                value = 1 + previous["occurrences"]
                cell = {
                    "occurrences": value,
                    "string": previous["string"] + char2
                }
                table[i][j] = cell
                if value > biggest_match["occurrences"]:
                    biggest_match = cell

    return biggest_match

word1 = 'fish'
word2 = 'wish'
s = find_longest_substring(word1, word2)
print("'{}' and '{}' have {} matches in '{}'".format(word1, word2, s['occurrences'], s['string']))

# Find the longest sequence
def find_matches(word1, word2):
    table = [[0 for __ in word2] for _ in word1]
    for i, char1 in enumerate(word1):
        for j, char2 in enumerate(word2):
            if char1 == char2:
                table[i][j] = table[i-1][j-1] + 1
            else:
                table[i][j] = max(table[i-1][j], table[i][j-1])

    return table[-1][-1]

word1 = 'fosh'
word2 = 'fort'
s = find_matches(word1, word2)
print("'{}' and '{}' have {} matches".format(word1, word2, s))

