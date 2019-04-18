def calculate_value(private, public_key, multiplier):
    # x =(9^4 mod 23) = (6561 mod 23) = 6
    value = (multiplier ** private) % public_key
    return value


def david_dancho_comunication(public_key, multiplier):
    # David  and Dancho get public Key = 23, Multiplier G = 9

    # David selected a private key a = 4 and
    # Dancho selected a private key b = 3
    david_public_value = calculate_value(4, 23, 9)
    dancho_public_value = calculate_value(3, 23, 9)

    david_symtric_key = calculate_value(dancho_public_value, 4, 23)
    dancho_symtric_key = calculate_value(david_public_value, 3, 23)

    if (david_symtric_key == dancho_symtric_key):
        print("Shared key is ", david_symtric_key)


david_dancho_comunication(23, 9)