import resources as res

allScores = []

### Quick Sort ###

def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

### Update Score List ###

def updateScoreList(score):
    if len(allScores) >= 10:
        if score > allScores[-1]:
            allScores[-1] = score
        else:
            pass
    else:
        allScores.append(score)

    n = len(allScores)
    quickSort(allScores, 0, n - 1)
    allScores.reverse()

def gloryHallTable(displayScreen):
    res.textSetting(displayScreen, (380, 230), res.statsCategoryFont, res.black, 'Top 10 runs:')
    for i in range(len(allScores)):
        res.textSetting(displayScreen, (400, 280 + i * 40), res.statsCategoryFont, res.black, f'{i+1}: {allScores[i]} points')

