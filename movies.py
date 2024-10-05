class Movie:
    def __init__ (self,name,year,director,rating,genre,cast):
        self.name = name
        self.year = year
        self.genre = genre
        self.director = director
        self.cast = cast
        self.rating =rating

    def set_name(self,value):
        self.name = value
    def set_year(self,value):
        self.year = value
    def set_director(self,value):
        self.director = value
    def set_rating(self,value):
        self.rating = value
    def set_genre(self,value):
        self.genre = value
    def set_cast(self,value):
        self.cast = value

    def get_name(self):
        return self.name
    def get_year(self):
        return self.year
    def get_director(self):
        return self.director
    def get_genre(self):
        return self.genre
    def get_rating(self):
        return self.rating
    def get_cast(self):
        return self.cast

    def __lt_name__ (self, other):
        return self.__name < other.name

    def __str__(self):
        return f"\nName: {self.name}\nYear: {self.year}\nRating: {self.rating}\nGenre: {self.genre}\nDirector: {self.director}\nCast: {self.cast}"



#Creating all the movies
m1 = Movie("The Shawshank Redemption", 1994, "Frank Darabont", "R", "Drama", "[Tim Robbins, Morgan Freeman]")
m2 = Movie("Pulp Fiction", 1994, "Quentin Tarantino", "R", "Crime", "[John Travolta, Uma Thurman, Samuel L. Jackson]")
m3 = Movie("The Godfather",1972,"Francis Ford Coppola","R","Crime","[Marlon Brando, Al Pacino, James Caan]")
m4 = Movie("Inception", 2010, "Christopher Nolan", "PG-13", "Sci-Fi", "[Leonardo DiCaprio, Joseph Gordon-Levitt, Ellen Page]")
m5 = Movie("The Matrix", 1999, "Lana Wachowski Lilly Wachowski", "R", "Sci-Fi", "[Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss]")
m6 = Movie("Forrest Gump", 1994, "Robert Zemeckis", "PG-13", "Drama", "[Tom Hanks, Robin Wright, Gary Sinise]")
m7 = Movie("The Dark Knight", 2008, "Christopher Nolan", "PG-13", "Action", "[Christian Bale, Heath Ledger, Aaron Eckhart]")
m8 = Movie("Fight Club", 1999, "David Fincher", "R", "Drama", "[Brad Pitt, Edward Norton, Helena Bonham Carter]")
m9 = Movie("Goodfellas", 1990,"Martin Scorsese", "R", "Crime", "[Robert De Niro, Ray Liotta, Joe Pesci]")
m10 = Movie("The Silence of the Lambs", 1991, "Jonathan Demme", "R", "Thriller", "[Jodie Foster, Anthony Hopkins, Scott Glenn]")
m11= Movie("Titanic", 1997, "James Cameron", "PG-13", "Romance", "[Leonardo DiCaprio, Kate Winslet, Billy Zane]")
m12= Movie("The Lord of the Rings: The Fellowship of the Ring", 2001, "Peter Jackson", "PG-13", "Fantasy", "[Elijah Wood, Ian McKellen, Orlando Bloom]")
m13= Movie("Gladiator", 2000, "Ridley Scott", "R", "Action", "[Russell Crowe, Joaquin Phoenix, Connie Nielsen]")
m14= Movie("The Green Mile", 1999, "Frank Darabont", "R", "Drama", "[Tom Hanks, Michael Clarke Duncan, David Morse]")
m15= Movie("Saving Private Ryan", 1998, "Steven Spielberg", "R", "War", "[Tom Hanks, Matt Damon, Tom Sizemore]")
m16= Movie("Jurassic Park", 1993, "Steven Spielberg", "PG-13", "Adventure", "[Sam Neill, Laura Dern, Jeff Goldblum]")
m17= Movie("The Departed", 2006, "Martin Scorsese", "R", "Crime", "[Leonardo DiCaprio, Matt Damon, Jack Nicholson]")
m18= Movie("The Lion King", 1994, "Roger Allers, Rob Minkoff", "G", "Animation", "[Matthew Broderick, Jeremy Irons, James Earl Jones]")
m19= Movie("Eternal Sunshine of the Spotless Mind", 2004, "Michel Gondry", "R", "Romance", "[Jim Carrey, Kate Winslet, Kirsten Dunst]")
m20= Movie("The Sixth Sense", 1999, "M. Night Shyamalan", "PG-13", "Thriller", "[Bruce Willis, Haley Joel Osment, Toni Collette]")
#putting in list
library = [m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13,m14,m15,m16,m17,m18,m19,m20]



def main(libray):
    choice = ""
    showMenu()
    while choice != "x":
        choice = input("What will you chose?: ")
        if choice == "?":
            showMenu()
        elif choice == "a":
            print(libray.sort())
        elif choice == "b":
            print (library.sort(key=lambda movie: movie.get_year()))
        elif choice == "c":
            listMovies(library)
        elif choice == "d":
            listGenre(library)
        elif choice == "e":
            searchDirector(library)
        elif choice == "f":
            searchCast(library)
        elif choice == "x":
            print("stopping program.")
        else:
            print("invalid input, try again.")
            showMenu()



def showMenu():
    print("\nTo sort the list alphabetically type a\nTo sort the list cronologically type b\nTo list all of the movies type c\nTo list all in a particual genre type d\nTo search movies made by a certain directer type e\nTo search movies by one of their cast members type f\nTo show the menu type ?\nTo exit the program type x")

def listMovies(library):
    for movie in library:
        print(movie)

def listGenre(library):
    genre = input("enter genre: ")
    results = 0
    for movie in library:
        temp = movie.get_genre(movie)
        if temp == genre:
            print(movie)
            results += 1
    print("movies found in your genre: " + str(results))

def searchDirector(library):
    director = input("what is the name of the director: ")
    results = 0
    for movie in library:
        temp = movie.get_director()
        if temp == director:
            print(movie)
            results += 1
    print("movies found with your director: "+ str(results))

def searchCast():
    actor = input("Name of the actor/actress you want to search for: ")
    results += 0
    for movie in library:
        temp = movie.get_cast()
        if actor in temp:
            print(movie)
            results +=1
    print("movies found with your actor/actress: " + str(results))


main(library)