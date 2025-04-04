from data_fetcher import fetch_data


def get_animal_name():
    """
    get animal name from user
    """
    while True:
        animal_name = input("Enter a name of an animal: ")
        if animal_name.strip() == "":
            print("Animal name cannot be empty.")
        else:
            return animal_name.strip().lower()


def get_and_display_skin_types_from_data(animals_list):
    """
    receives a list of animal info and get all skin types
    """
    skin_types = []
    for animal in animals_list:
        # will only take the animals with skin type info into account
        if "characteristics" in animal and "skin_type" in animal["characteristics"]:
            if animal["characteristics"]["skin_type"].lower().strip() not in skin_types:
                skin_types.append(animal["characteristics"]["skin_type"].lower().strip())
    print("Hi! There are {} skin types: ".format(len(skin_types)))
    for skin in skin_types:
        print(skin)
    print()
    return skin_types


def get_skin_type_from_user(skin_types):
    """
    ask user to input valid skin type
    """
    while True:
        skin_type = input("Enter a skin type from above to display the animals (Enter 0 to display all): ")
        if skin_type.lower().strip() in skin_types:
            return skin_type.lower().strip()
        elif skin_type.strip() == "0":
            return skin_type.strip()
        else:
            print("Please enter a valid skin type.")


def filter_animal_skin_type(skin_type, animal_list):
    """
    receives a list of data and a skin type keyword, filter out animal with that skin type
    """
    filtered_animal_list = []
    for animal in animal_list:
        if "characteristics" in animal and "skin_type" in animal["characteristics"]:
            if skin_type == animal["characteristics"]["skin_type"].lower().strip():
                filtered_animal_list.append(animal)
    return filtered_animal_list


def serialize_animal(animal_obj):
    """
    receives a dictionary and return its info as formatted html text
    """
    # collect needed info
    name = animal_obj.get("name")
    animal_char = animal_obj.get("characteristics")
    animal_diet = animal_char.get("diet") if animal_char else None
    animal_type = animal_char.get("type") if animal_char else None
    animal_slogan = animal_char.get("slogan") if animal_char else None
    locations = animal_obj.get("locations")
    # format the info to html text
    animal_data_text = "<li class='cards__item'>"
    if name:
        animal_data_text += f"<div class='card__title'>{name}</div>\n"
    animal_data_text += "<div class='card__text'>\n<ul>"
    if animal_diet:
        animal_data_text += f"<li><strong>Diet: </strong>{animal_diet}</li>\n"
    if locations is not None and len(locations) > 0:
        animal_data_text += f"<li><strong>Location: </strong>{locations[0]}</li>\n"
    if animal_type:
        animal_data_text += f"<li><strong>Type: </strong>{animal_type}</li>\n"
    if animal_slogan:
        animal_data_text += f"<li><strong>Slogan: </strong>{animal_slogan}</li>\n"
    animal_data_text += "</ul></div></li>"
    return animal_data_text


def generate_animal_data_string(animals_data):
    """
    returning organized text as string from a json file carrying nested data structure
    """
    output = ""
    # loop through and collect info for each animal, update the text
    for animal in animals_data:
        output += serialize_animal(animal)
    # return text string
    return output


def read_html(file_path):
    """
    read html file and return html content
    """
    with open(file_path, "r") as f:
        return f.read()


def update_animal_html(old_str, new_str):
    """
    take a html template and replace placeholder string with target data string
    """
    text = read_html("animals_template.html")
    text = text.replace(old_str, new_str)
    with open("animals.html", "w") as f:
        f.write(text)


def main():
    """
    get animal info from a json file, select skin type, and display animal data in a html file
    """
    animal_name = get_animal_name()
    animals_data = fetch_data(animal_name)
    if animals_data is None:
        animals_text = "<h2><i>Error retrieving animal data! Please try again.</i></h2>"
    elif not animals_data:
        animals_text = f"<h2><i>The animal <strong style='color: firebrick'>'{animal_name}'</strong> doesn't exist.</i></h2>"
    else:
        skin_types = get_and_display_skin_types_from_data(animals_data)
        skin_type = get_skin_type_from_user(skin_types)
        if skin_type == "0":
            animals_text = generate_animal_data_string(animals_data)
        else:
            filtered_animals_data = filter_animal_skin_type(skin_type, animals_data)
            animals_text = generate_animal_data_string(filtered_animals_data)
    update_animal_html("__REPLACE_ANIMALS_INFO__", animals_text)
    print("Website was successfully generated to the file animals.html.")


if __name__ == "__main__":
    main()
