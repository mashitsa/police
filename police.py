import os

directory = os.getcwd()


def main():
    count_rows = {}
    files = [file for file in os.listdir(directory) if os.path.isfile(f'{directory}/{file}')]
    for file in files:
        txt = open(f'{directory}/{file}', encoding='UTF=8')
        count_rows[file] = len(txt.readlines())
        txt.close()
    sorted_count_rows = sorted(count_rows, key=count_rows.get)

    for file in sorted_count_rows:
        txt = open(f'{directory}/{file}', encoding="UTF-8")
        with open('out.txt', 'a', encoding="UTF-8") as my_file:
            my_file.write(file + '\n')
            my_file.write(str(count_rows[file]) + '\n')
            my_file.write(''.join(txt.readlines()) + '\n')
        txt.close()


if __name__ == "__main__":
    main()
