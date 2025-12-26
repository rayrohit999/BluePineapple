def sortList(arr : list[tuple[int,...]]) -> list[tuple[int,...]]:
    return sorted(arr,key = lambda x : x[0])

if __name__ == "__main__":
    print(sortList([(3,5,8,4,6),(3,4,5,6,7)]))