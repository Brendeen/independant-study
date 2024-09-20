import os
import re


def read_template(path):
    if not os.path.exists(path):
        raise FileNotFoundError
    with open(path, "r") as file:
        content = file.read()
        # print(content)
        return content


def parse_template(content):
    find_all_list = re.findall(r'{(.*?)}', content)
    new_string = re.sub(r'({.*?})', '{}', content)
    find_all_list = tuple(find_all_list)
    # print(new_string)
    # print(find_all_list)
    return new_string, find_all_list


def merge(new_string, find_all_list):
    final_string = new_string.format(*find_all_list)
    # print(final_string)
    return final_string


def mb():
    name = input(f"""
    Welcome to my Madlib, please tell me your name...
    > """)
    print(f"""
    Nice to meet you {name}
    """)

    content = read_template("assets/dark_and_stormy_night_template.txt")
    new_string, placeholders = parse_template(content)
    user_answers = []
    for placeholder in placeholders:
        answer = input(f"""Provide me with a {placeholder}.
        > """)
        user_answers.append(answer)

    final_mb = merge(new_string, user_answers)

    print(f"""
    Thank you {name},
    your final Madlib is...
    {final_mb}
    """)


if __name__ == "__main__":
    mb()
