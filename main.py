def test(arr):
    if (len(arr) == 0): return False;
    if(arr[0] == arr[-1]): return True;
    else: return False;
print(test([1, 1]))
