# https://www.codevoila.com/post/45/open-web-browser-window-or-new-tab-with-python
# https://www.geeksforgeeks.org/reading-writing-text-files-python/
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



if __name__ == '__main__':

    current_film = URL_Generator()

    movie_list = current_film.open_a_file("Movies")
    for film in movie_list:
        print(current_film.create_url(film, "Amazon"))
        # print(current_film.create_url(film, "Netflix"))
        # print(current_film.create_url(film, "Xfinity"))

    current_film.write_to_file("Urls_Amazon_Films")

