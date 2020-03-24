class FileWriter:

    def __init__(self):
        filename = ""


    def read_films_from_file(self, filename):
        file = open(filename)
        initial_film_list = file.readlines()
        list_of_films = []
        for x in range(len(initial_film_list)):
            cur_film = initial_film_list[x]
            substring_film = cur_film[0:len(cur_film) - 1]
            list_of_films.insert(x, substring_film)
            # print(list_of_films[x])

        file.close()
        return list_of_films

    def write_to_file(self, filename):
        file = open(filename, "w")
        file.write("Testing\n")
        file.write("Testing\n")
        file.write("1\n")
        file.write("2\n")
        file.write("1\n")
        file.write("2\n")
        file.close()