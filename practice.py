# Write your code here :-)
def foo(bar):
    bar = 3
    print(bar)
    return bar + 2

bar = 10
foo(bar)
print(bar)
baz = foo(bar)
print(bar)
print(baz)
bar = foo(bar)
print(bar)
print(baz)
