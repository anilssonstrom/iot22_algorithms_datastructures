

# Från 0 till 1000:
# Om jämt delbart med 3 eller 5: Summera

def even_3_5_sum(limit):
    s = 0

    for number in range (0, limit):
        # Om number är delbart med 3 eller 5, addera det till s
        if number % 3 == 0 or number % 5 == 0:
            s += number

    return s


if __name__ == '__main__':
    print(even_3_5_sum(10))  # Ska bli 23
    print(even_3_5_sum(1000))
    # 3+5+6+9 = 23