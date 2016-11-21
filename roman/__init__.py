def _ones_to_roman(ones):
    if ones == 4:
        return "IV"
    elif ones == 9:
        return "IX"
    else:
        if ones >= 5:
            roman = "V"
            ones -= 5
        else:
            roman = ""
        return roman + "I" * ones


def _tens_to_roman(tens):
    if tens == 4:
        return "XL"
    # elif tens == 9:
    #     return "IX"
    else:
        # if tens >= 5:
        #     roman = "V"
        #     tens -= 5
        # else:
        #     roman = ""
        roman = ""
        return roman + "X" * tens


def arabic_to_roman(arabic):
    if arabic > 0 and arabic < 4000:
        if arabic < 10:
            return _ones_to_roman(arabic)
        else:
            return _tens_to_roman(arabic / 10)
    else:
        raise RuntimeError("Arabic number must be positive and less than 4000")