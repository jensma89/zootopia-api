from fetch_animals import fetch_animals_data
import os

def get_html_data(file_path):
    """Load the data from HTML file."""
    try:
        with open(file_path, "r") as fileobject:
            return fileobject.read()
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return ""


def convert_animals_data_to_str(animals_data, search_input):
    """Convert the animals data to a string and return it,
     only showing existing fields."""
    if not animals_data:
        return (f'<h2 style="text-align: center;">'
                f'The animal "{search_input}" '
                f'doesn\'t exist!</h2>')
    animal_output = ""
    for animal in animals_data:
        animal_output += '<li class="cards__item">'
        animal_output += (f'<div class="card_title">'
                          f'{animal.get("name")}</div><br/>\n')
        animal_output += '<p class="card__text">'

        characteristics = animal.get('characteristics', {})

        if 'diet' in characteristics:   # Check if diet exist
            animal_output += (f'<strong>Diet:</strong> '
                              f'{characteristics["diet"]}<br/>\n')

        if animal.get('locations'): # Check if location exist
            animal_output += (f'<strong>Location:</strong> '
                              f'{animal["locations"][0]}<br/>\n')

        if 'type' in characteristics:   # Check if type exist
            animal_output += (f'<strong>Type:</strong> '
                              f'{characteristics["type"]}<br/>\n')

            animal_output += '</p>'
        animal_output += '</li>'

    return animal_output


def write_new_animals_html(template_path, output_filename, animals_info):
    """Write the animals data to a new HTML file in the 'static' folder."""

    # Check is statics folder already exist
    os.makedirs("static", exist_ok=True)

    html_template = get_html_data(template_path)
    html_output = html_template.replace("__REPLACE_ANIMALS_INFO__",
                                        animals_info)

    output_path = os.path.join("static", output_filename)

    with open(output_path, "w") as fileobject:
        fileobject.write(html_output)


def main():
    """Ask the user to search an animal
    and call the functions."""
    search_input = input("Enter a animal: ").lower().strip()
    animals_data = fetch_animals_data(search_input)
    animals_output = convert_animals_data_to_str(animals_data, search_input)
    write_new_animals_html("animals_template.html",
                           "animals.html", animals_output)

if __name__ == "__main__":
    main()
