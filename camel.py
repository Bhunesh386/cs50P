# camel.py

def camel_to_snake(name):
    snake_case = ""
    for c in name:
        if c.isupper():
            snake_case += "_" + c.lower()
        else:
            snake_case += c
    return snake_case

def main():
    camel_case_name = input("Enter a camel case variable name: ")
    snake_case_name = camel_to_snake(camel_case_name)
    print("Snake case variable name:", snake_case_name)

if __name__ == "__main__":
    main()
