def function(num):
    if num <= 1:
        return
    function(num - 1)
    print(num, end=" ")
    function(num - 1)

function(5)

def facto(n):
    if n <= 1:
        return 1
    return n * facto(n-1)

c = facto(5)
print(c)