messy_names = ["  alice ", "Bob", " charlie", "Alice", "BOB ", "eve  ", " Eve", "eve"]

def clean_names(names):
    clean_names = []
    for name in names:
        clean_names.append(name.strip().capitalize())
    return clean_names

if __name__ == "__main__":
    print(clean_names(messy_names))