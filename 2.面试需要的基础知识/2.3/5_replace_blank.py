def replace_blank(string: str):
    string.replace(" ", "%020")

if __name__ == '__main__':
    s = "we are happy!"
    print(replace_blank())