def solve(numheads, numlegs):

    rabbits = (numlegs - numheads * 2)/2
    chickens = numheads - rabbits
    print(f"R:{rabbits},C:{chickens}")



heads = int(input())
legs = int(input())
solve(heads,legs)