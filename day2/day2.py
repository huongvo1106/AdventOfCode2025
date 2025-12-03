sampleStr = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
realStr = "6161588270-6161664791,128091420-128157776,306-494,510-1079,10977-20613,64552-123011,33-46,28076-52796,371150-418737,691122-766624,115-221,7426210-7504719,819350-954677,7713444-7877541,63622006-63661895,1370-1981,538116-596342,5371-8580,8850407-8965070,156363-325896,47-86,452615-473272,2012-4265,73181182-73335464,1102265-1119187,3343315615-3343342551,8388258268-8388317065,632952-689504,3-22,988344-1007943"


myList = realStr.split(",")
print(myList)

totalDouble = 0
for item in myList:
    print("New Item")
    dashPos = item.index("-")
    firstId = item[0:dashPos]
    firstIdLen = len(firstId)
    lastId = item[dashPos + 1:]
    lastIdLen = len(lastId)

    checkInt = int(firstId)
    while (checkInt <= int(lastId)):
        #only check number whose len is an even number
        checkStr = str(checkInt)
        print("checkStr",checkStr)
        if (len(checkStr) % 2 == 0):
            halfPoint = int(len(checkStr) / 2)
            print("Half point ",halfPoint)
            if (checkStr[0:halfPoint] == checkStr[halfPoint:]):
                totalDouble += checkInt
            checkInt += 1
            checkStr = str(checkInt)
        else:
            checkStr = "1" + "0" * len(checkStr)
            checkInt = int(checkStr)
    print("Result wip ",totalDouble)


print("Result ", totalDouble)

#this method got the correct result: 19574776074. This should be optimal.
