def manipulate_string(txt):
    encode_txt = ""
    size = len(txt)
    i = 0
    while i < size:
        current_charcter = txt[i]
        repeat_symbols = 1
        for j in range(i + 1, size):
            if txt[i] == txt[j]:
                repeat_symbols = repeat_symbols + 1
            else:
                break
        if repeat_symbols == 1:
            encode_txt = encode_txt + txt[i]
            i = i + 1
        else:
            encode_txt = encode_txt + str(repeat_symbols) + current_charcter
            i = i + repeat_symbols
    return txt


def test(txt):
    size = len(txt)
    k = 0
    for i in range(k, size):
        # print(i)
        print(str(i) + " " + txt[i])
        k = k + 1


manipulate_string("ABCCCDDK")
test("ABCC")


# manipulate_string("ABCC")
#
def encode(txt):
    """
    Returns the run-length encoded version of the text
    (numbers after symbols, length = 1 is skipped)
    """
    encode_txt = ""
    size = len(txt)
    i = 0
    while i < size:
        current_char = txt[i]
        repeat_symbols = 1
        for j in range(i + 1, size):
            if txt[i] == txt[j]:
                repeat_symbols = repeat_symbols + 1
            else:
                break
        if repeat_symbols == 1:
            encode_txt = encode_txt + txt[i]
            i = i + 1
        else:
            encode_txt = encode_txt + current_char + str(repeat_symbols)
            i = i + repeat_symbols
    return encode_txt


print('16'.isdigit())


def decode(txt):
    """
    Decodes the text using run-length encoding
    """
    size = len(txt)
    i = 0
    txt_result = ""
    while i < size:

        repetable = 0
        current_char = txt[i]
        if current_char.isdigit():
            repetable = int(current_char) - 1
            for j in range(0, repetable):
                txt_result = txt_result + txt[i - 1]
            i = i + 1
        else:
            txt_result = txt_result + current_char
            i = i + 1
    print(txt_result)
    return txt_result


# # Tests
# # Test that the functions work on their own
print(encode("AABCCCDEEEE"))
assert encode("AABCCCDEEEE") == "A2BC3DE4"
assert decode("A2BC3DE4") == "AABCCCDEEEE"

# # Test that the functions really invert each other
assert decode(encode("AABCCCDEEEE")) == "AABCCCDEEEE"
assert encode(decode("A2BC3DE4")) == "A2BC3DE4"


