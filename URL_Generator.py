# https://www.codevoila.com/post/45/open-web-browser-window-or-new-tab-with-python
# https://www.geeksforgeeks.org/reading-writing-text-files-python/

import webbrowser


class URL_Generator:

    def __init__(self):
        self.connection = None
        self.title = ""
        self.netflix_base_url = "https://www.netflix.com/search?q="
        self.amazon_base_url = "https://www.amazon.com/s?k="
        self.amazon_base_url_end_tag = "&i=prime-instant-video"
        self.xfinity_base_url = "https://www.xfinity.com/stream/search?q="
        self.complete_url = ""

    def create_url(self, title, platform):
        split_str = title.split(" ")
        query_str = ""
        for cur_word in split_str:
            if platform == "Amazon":
                query_str += cur_word + "+"
            else:
                query_str += "%20" + cur_word

        if platform == "Amazon":
            query_str = query_str[0:len(query_str) - 1]
            self.complete_url = self.amazon_base_url + query_str + self.amazon_base_url_end_tag
        elif platform == "Netflix":
            self.complete_url = self.netflix_base_url + query_str
        else:
            self.complete_url = self.xfinity_base_url + query_str

        return self.complete_url

    def open_a_file(self, filename):
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

    def write_to_file(self, filename, list_to_write):
        file = open(filename,"w")
        for url in list_to_write:
            file.write(url + "\n")
        file.close()

if __name__ == '__main__':

    generator = URL_Generator()
    # Collect URLS
    # OPEN Links
    movie_list = generator.open_a_file("Movies")

    initial_command = input("What would you like to do (type the number)\n1. Update Links\n2. Open Links\n3. Exit\n")

    while not initial_command.isdigit() or int(initial_command) != 3:
        if not initial_command.isdigit() or int(initial_command) <1 or int(initial_command) >2:
            initial_command = input("What would you like to do (type the number)\n1. Update Links\n2. Open Links\n3. Exit\n")
        else:

            platform = input("What platform are you using?\n")
            while platform not in ['Amazon', 'Netflix', 'Xfinity']:
                platform = input("What platform are you using? (Amazon, Netflix or Xfinity)\n")

            if initial_command == 1:
                # Write to file
                url_list = []
                for film in movie_list:
                    url = generator.create_url(film, platform)
                    url_list.append(url)

                if platform == "Amazon":
                    file_name = "Urls_Amazon_Films"
                elif platform == "Netflix":
                    file_name = "Urls_Netflix_Films"
                else:
                    file_name = "Urls_Xfinity_Films"

                generator.write_to_file(file_name, url_list)
            else:


            initial_command = input("What would you like to do (type the number)\n1. Update Links\n2. Open Links\n3. Exit\n")







