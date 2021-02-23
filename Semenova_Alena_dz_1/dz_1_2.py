values = []
i = 1
while i < 1000:
    if i % 2 != 0:
        value = i ** 3
        values.append(value)
    i += 1
all_sum = 0
for value in values:
    if value < 100:
        one = value // 10
        two = value - one * 10
        sum = one + two
        if sum // 7: all_sum += sum
    elif value < 1000:
        one = value // 100
        two = (value - one * 100) // 10
        three = value - one * 100 - two * 10
        sum = one + two + three
        if sum // 7: all_sum += sum
    elif value < 10000:
        one = value // 1000
        two = (value - one * 1000) // 100
        three = (value - one * 1000 - two * 100) // 10
        four = value - one * 1000 - two * 100 - three * 10
        sum = one + two + three + four
        if sum // 7: all_sum += sum
    elif value < 100000:
        one = value // 10000
        two = (value - one * 10000) // 1000
        three = (value - one * 10000 - two * 1000) // 100
        four = (value - one * 10000 - two * 1000 - three * 100) //10
        fifth = value - one * 10000 - two * 1000 - three * 100 - four * 10
        sum = one + two + three + four + fifth
        if sum // 7: all_sum += sum
    elif value < 1000000:
        one = value // 100000
        two = (value - one * 100000) // 10000
        three = (value - one * 100000 - two * 10000) // 1000
        four = (value - one * 100000 - two * 10000 - three * 1000) //100
        fifth = (value - one * 100000 - two * 10000 - three * 1000 - four * 100) // 10
        six = value - one * 100000 - two * 10000 - three * 1000 - four * 100 - fifth * 10
        sum = one + two + three + four + fifth + six
        if sum // 7: all_sum += sum
    elif value < 10000000:
        one = value // 1000000
        two = (value - one * 1000000) // 100000
        three = (value - one * 1000000 - two * 100000) // 10000
        four = (value - one * 1000000 - two * 100000 - three * 10000) //1000
        fifth = (value - one * 1000000 - two * 100000 - three * 10000 - four * 1000) // 100
        six = (value - one * 1000000 - two * 100000 - three * 10000 - four * 1000 - fifth * 100) //10
        seven = value - one * 1000000 - two * 100000 - three * 10000 - four * 1000 - fifth * 100 - six * 10
        sum = one + two + three + four + fifth + six + seven
        if sum // 7: all_sum += sum
    elif value < 100000000:
        one = value // 10000000
        two = (value - one * 10000000) // 1000000
        three = (value - one * 10000000 - two * 1000000) // 100000
        four = (value - one * 10000000 - two * 1000000 - three * 100000) //10000
        fifth = (value - one * 10000000 - two * 1000000 - three * 100000 - four * 10000) // 1000
        six = (value - one * 10000000 - two * 1000000 - three * 100000 - four * 10000 - fifth * 1000) //100
        seven = (value - one * 10000000 - two * 1000000 - three * 100000 - four * 10000 - fifth * 1000 - six * 100) // 10
        eight = value - one * 10000000 - two * 1000000 - three * 100000 - four * 10000 - fifth * 1000 - six * 100 - seven * 10
        sum = one + two + three + four + fifth + six + seven + eight
        if sum // 7: all_sum += sum
    elif value >= 100000000:
        one = value // 100000000
        two = (value - one * 100000000) // 10000000
        three = (value - one * 100000000 - two * 10000000) // 1000000
        four = (value - one * 100000000 - two * 10000000 - three * 1000000) // 100000
        fifth = (value - one * 100000000 - two * 10000000 - three * 1000000 - four * 100000 ) // 10000
        six = (value - one * 100000000 - two * 10000000 - three * 1000000 - four * 100000 - fifth * 10000) // 1000
        seven = (value - one * 100000000 - two * 10000000 - three * 1000000 - four * 100000 - fifth * 10000 - six * 1000) // 100
        eight = (value - one * 100000000 - two * 10000000 - three * 1000000 - four * 100000 - fifth * 10000 - six * 1000 - seven * 100) // 10
        nine = value - one * 100000000 - two * 10000000 - three * 1000000 - four * 100000 - fifth * 10000 - six * 1000 - seven * 100 - eight * 10
        sum = one + two + three + four + fifth + six + seven + eight + nine
        if sum // 7:
            all_sum += sum
    else: print("Что-то пошло не так!")
print(all_sum)
for idx in range(len(values)):
    values[idx] += 17
all_sum = 0
for value in values:
    if value < 100:
        one = value // 10
        two = value - one * 10
        sum = one + two
        if sum // 7: all_sum += sum
    elif value < 1000:
        one = value // 100
        two = (value - one * 100) // 10
        three = value - one * 100 - two * 10
        sum = one + two + three
        if sum // 7: all_sum += sum
    elif value < 10000:
        one = value // 1000
        two = (value - one * 1000) // 100
        three = (value - one * 1000 - two * 100) // 10
        four = value - one * 1000 - two * 100 - three * 10
        sum = one + two + three + four
        if sum // 7: all_sum += sum
    elif value < 100000:
        one = value // 10000
        two = (value - one * 10000) // 1000
        three = (value - one * 10000 - two * 1000) // 100
        four = (value - one * 10000 - two * 1000 - three * 100) //10
        fifth = value - one * 10000 - two * 1000 - three * 100 - four * 10
        sum = one + two + three + four + fifth
        if sum // 7: all_sum += sum
    elif value < 1000000:
        one = value // 100000
        two = (value - one * 100000) // 10000
        three = (value - one * 100000 - two * 10000) // 1000
        four = (value - one * 100000 - two * 10000 - three * 1000) //100
        fifth = (value - one * 100000 - two * 10000 - three * 1000 - four * 100) // 10
        six = value - one * 100000 - two * 10000 - three * 1000 - four * 100 - fifth * 10
        sum = one + two + three + four + fifth + six
        if sum // 7: all_sum += sum
    elif value < 10000000:
        one = value // 1000000
        two = (value - one * 1000000) // 100000
        three = (value - one * 1000000 - two * 100000) // 10000
        four = (value - one * 1000000 - two * 100000 - three * 10000) //1000
        fifth = (value - one * 1000000 - two * 100000 - three * 10000 - four * 1000) // 100
        six = (value - one * 1000000 - two * 100000 - three * 10000 - four * 1000 - fifth * 100) //10
        seven = value - one * 1000000 - two * 100000 - three * 10000 - four * 1000 - fifth * 100 - six * 10
        sum = one + two + three + four + fifth + six + seven
        if sum // 7: all_sum += sum
    elif value < 100000000:
        one = value // 10000000
        two = (value - one * 10000000) // 1000000
        three = (value - one * 10000000 - two * 1000000) // 100000
        four = (value - one * 10000000 - two * 1000000 - three * 100000) //10000
        fifth = (value - one * 10000000 - two * 1000000 - three * 100000 - four * 10000) // 1000
        six = (value - one * 10000000 - two * 1000000 - three * 100000 - four * 10000 - fifth * 1000) //100
        seven = (value - one * 10000000 - two * 1000000 - three * 100000 - four * 10000 - fifth * 1000 - six * 100) // 10
        eight = value - one * 10000000 - two * 1000000 - three * 100000 - four * 10000 - fifth * 1000 - six * 100 - seven * 10
        sum = one + two + three + four + fifth + six + seven + eight
        if sum // 7: all_sum += sum
    elif value >= 100000000:
        one = value // 100000000
        two = (value - one * 100000000) // 10000000
        three = (value - one * 100000000 - two * 10000000) // 1000000
        four = (value - one * 100000000 - two * 10000000 - three * 1000000) // 100000
        fifth = (value - one * 100000000 - two * 10000000 - three * 1000000 - four * 100000 ) // 10000
        six = (value - one * 100000000 - two * 10000000 - three * 1000000 - four * 100000 - fifth * 10000) // 1000
        seven = (value - one * 100000000 - two * 10000000 - three * 1000000 - four * 100000 - fifth * 10000 - six * 1000) // 100
        eight = (value - one * 100000000 - two * 10000000 - three * 1000000 - four * 100000 - fifth * 10000 - six * 1000 - seven * 100) // 10
        nine = value - one * 100000000 - two * 10000000 - three * 1000000 - four * 100000 - fifth * 10000 - six * 1000 - seven * 100 - eight * 10
        sum = one + two + three + four + fifth + six + seven + eight + nine
        if sum // 7:
            all_sum += sum
    else: print("Что-то пошло не так!")
print(all_sum)



