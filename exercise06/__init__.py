def task5counter(n):
    counter = 0
    counter2 = 0
    for i in range(0, int(pow(2, n))):
        test_string = ""
        test_string = format(i, 'b')
        # time.sleep(2)
        while len(test_string) != n:
            test_string = "0" + test_string
            # print(test_string + " ist " + str(i) + " Zeile 10")
        if test_condition(test_string):
            counter += 1
        if test_condition2(test_string):
            counter2 += 1
    print(str(n) + ": " + str(counter) + "/" + str(pow(2, n)) + ", d.h.: " + str(
        counter / pow(2, n) * 100) + "% erfüllen die Bedinung! vs " + str(counter2) + "/" + str(
        pow(2, n)) + ", d.h.: " + str(counter2 / pow(2, n) * 100) + "%")


def test_condition(
        testString):  # https://oeis.org/search?q=0%2C0%2C0%2C0%2C1%2C2%2C7%2C16%2C38&language=german&go=Suche
    # print("testCondition called on: " + testString)
    n = len(testString)
    counter101 = occurrences(testString, "101")
    counter010 = occurrences(testString, "010")
    # if counter010 * 2 == counter101 and counter101 != 0:
    #     return True
    if counter010 * 2 == counter101:
        return True
    return False


def test_condition2(
        testString):  # https://oeis.org/search?q=2%2C4%2C6%2C10%2C17%2C28%2C49%2C84&sort=&language=german&go=Suche
    # print("testCondition called on: " + testString)
    n = len(testString)
    counter101 = occurrences(testString, "101")
    counter010 = occurrences(testString, "010")
    if counter010 * 2 == counter101 and counter101 != 0:
        return True
    return False


def occurrences(string, sub):
    count = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count += 1
        else:
            return count


def main():
    for i in range(1, 16):
        task5counter(i)


if __name__ == "__main__":
    # execute only if run as a script
    main()
