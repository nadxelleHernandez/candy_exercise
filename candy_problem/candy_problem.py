'''
1. 
In `get_friends_favorite_candy_count()`, return a dictionary of candy names 
and the amount of times each candy appears in the `friend_favorites` list.

friend_favorites = [
    ["Sally", ["lollipop", "bubble gum", "laffy taffy" ]],
    ["Bob", ["milky way", "licorice", "lollipop" ]],
    ["Arlene", ["chocolate bar", "milky way", "laffy taffy" ]],
    ["Carlie", ["nerds", "sour patch kids", "laffy taffy" ]]
]
'''
def get_friends_favorite_candy_count(favorites):
    if favorites is None:
        return None

    favorites_count = dict()
    for friends in favorites:
        for candy in friends[1]:
            if candy not in favorites_count:
                favorites_count[candy]=1
            else:
                favorites_count[candy]+=1

    return favorites_count

'''
2. 
Given the list `friend_favorites`, create a new data structure in the 
function `create_new_candy_data_structure` that describes the different 
kinds of candy paired with a list of friends that like that candy. 

friend_favorites = [
    ["Sally", ["lollipop", "bubble gum", "laffy taffy" ]],
    ["Bob", ["milky way", "licorice", "lollipop" ]],
    ["Arlene", ["chocolate bar", "milky way", "laffy taffy" ]],
    ["Carlie", ["nerds", "sour patch kids", "laffy taffy" ]]
]
'''
def create_new_candy_data_structure(data):
    if data is None :
        return None

    favorite_candy = dict()
    for friends in data:
        friend = friends[0]
        for candy in friends[1]:
            if candy not in favorite_candy:
                favorite_candy[candy] = list()
                favorite_candy[candy].append(friend)
            else:
                favorite_candy[candy].append(friend)

    return favorite_candy


'''
3. 
In `get_friends_who_like_specified_candy()`, return a tuple of 
friends who like the candy specified in the candy_name parameter.
'''
def get_friends_who_like_specific_candy(data, candy_name):
    favorite_candies = create_new_candy_data_structure(data)

    if favorite_candies is None or not candy_name:
        return None

    return tuple(favorite_candies[candy_name])

'''
4. 
In, `create_candy_set()`, return a set of all the candies from
the data structure made in `create_new_candy_data_structure()`.
'''
def create_candy_set(data):
    favorites = create_new_candy_data_structure(data)

    return set(favorites.keys())

'''
5. 
Starting with nominal cases, write tests for each of the functions 
in the file tests/test_candy_data_structure.py then write tests to 
handle edge cases.
'''

friend_favorites = [
    ["Sally", ["lollipop", "bubble gum", "laffy taffy" ]],
    ["Bob", ["milky way", "licorice", "lollipop" ]],
    ["Arlene", ["chocolate bar", "milky way", "laffy taffy" ]],
    ["Carlie", ["nerds", "sour patch kids", "laffy taffy" ]]
]

favorites_count = get_friends_favorite_candy_count(friend_favorites)
print(favorites_count)

favorite_candy = create_new_candy_data_structure(friend_favorites)
print(favorite_candy)