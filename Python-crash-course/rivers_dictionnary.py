"""Make a dictionnary containing three major rivers and the country each river runs through
one key-value pair might be 'nile' : 'egypt


1. Use a loop to print a sentence about each river, such as Nile river run through Egypt'
2. Use a loop to print the name of each river included in the dictionnary'
3. Use a loop to print the name of each country included in the dictionnary'
"""

country_rivers = {
    "loire": "france",
    "creuse": "france",
    "matapedia": "canada",
    "colorado": "usa",
    "rio vero": "spain",
}


def say_in_which_country(country_river: dict) -> str:
    """This function returns a string containing the key-value pair of the dictionnary"""
    for river in country_river.keys():
        print(f"{river.title() } is in {country_river[river].title() }")


def get_rivers(country_river: dict) -> str:
    for river in country_river.keys():
        print(f"The rivers are {river.title()}")


def get_countries(country_river: dict) -> list:
    for country in country_rivers.values():
        print(f"Here are the countries of the dictionnary {country.title()}")


favorites_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
    "maria": "",
    "nicolas": "",
    "remi": "",
}

"""Polling : use the code in favorite language
Make a list of people who should take the favorite language poll include some names
 that are already in the dictionnary and some that are not.
 
 Loop though the list of people who should take the poll. If they have already taken the poll,
 print a message thanking them for responding if they have not yet taken the poll,
 print a message inviting them to take the poll
 """

for name in favorites_languages.keys():
    if favorites_languages[name] == "":
        print(f"{name.title()}, You've  note yet taken the poll, please take the poll.")
    else:
        print(f"{name.title()}, thanks for answering.")
