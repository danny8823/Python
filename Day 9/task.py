# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again.",
#     "Loop": "The action of doing something over and over again."
# }

# # print(programming_dictionary["Bug"])

# programming_dictionary["Variable"] = "The name of the data which data is assigned to."

# # print(programming_dictionary)

# for key in programming_dictionary:
#     print(key + ':' + ' ' + programming_dictionary[key])

capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

travel_log = {
    "France": {
        "num_times_visited": 8,
        "cities_visited": [
            "Paris",
            "Lille",
            "Dijon"
        ]
    }
}

print(travel_log["France"]["cities_visited"][1])
capitals[1] = 4
print(capitals)
# nested_list = ['A', 'B', ['C', 'D']]

# print(nested_list[2][0])
