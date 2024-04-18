import string


def remove_whitespace(s: str):
    return s.replace(" ", "")


def remove_punctuation(s: str):
    return s.translate(s.maketrans("ad", "xz", string.punctuation))


def remove_numbers(s: str):
    return s.translate(s.maketrans("", "", string.digits))


def reverse(s: str):
    return "".join(s.split(" ")[::-1])


def to_lower_case(s: str):
    return s.lower()


def to_upper_case(s: str):
    return s.upper()


def is_palindrome(s: str):
    return s == s[::-1]


def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)


def count_substrings(s: str, sub: str):
    count = 0
    start = 0
    while True:
        start = s.find(sub, start) + 1
        if start > 0:
            count += 1
        else:
            break
    return count


def replace_substring(s: str, old_sub: str, new_sub: str):
    return s.replace(old_sub, new_sub)




