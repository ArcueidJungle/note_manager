import string


def is_palindrome(s):
    s = s.lower().translate(str.maketrans('','', string.punctuation)).replace(' ','')
    return s == s[::-1]

def main():
    s = input('введите строку')
    print(is_palindrome(s))

if __name__ == '__main__':
    main()
