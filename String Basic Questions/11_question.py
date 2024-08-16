# Python | Count the Number of matching characters in a pair of string

def count_matching_chars(str1,str2):
    s1 = set(str1)
    s2 = set(str2)
    return (len((s1).intersection((s2))))

str1 = "abcd"
str2 = "abef"
common = count_matching_chars(str1, str2)
print(common)

