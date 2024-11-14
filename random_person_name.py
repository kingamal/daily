import random

def load_names(filename):
    with open(filename, 'r') as file:
        names = file.readlines()
    return names

def random_name(names):
    selected_name = random.choice(names)
    selected_name = selected_name[:-2]
    return selected_name

def display_name(name):
    print(f'Randomly selected name: {name}')

def main():
    names = load_names('names.txt')
    selected_name = random_name(names)
    display_name(selected_name)

if __name__ == "__main__":
    main()