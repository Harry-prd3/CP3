class Movie:
    def __init__ (self,name,year,director,rating,genre,cast):
        self.name = name
        self.year = year
        self.genre = genre
        self.director = director
        self.cast = cast
        self.rating =rating

    def sort_alpha(self, movie2, movie3, movie4, movie5, movie6, movie7, movie8,movie9,movie10):
        movieNames = [self.name, movie2.name, movie3.name, movie4.name, movie5.name, movie6.name, movie7.name, movie8.name,movie9.name,movie10.name]
        movieNames.sort()
        return(movieNames)

    def sort_crono(self, movie2, movie3, movie4, movie5, movie6, movie7, movie8,movie9,movie10):
        movieyears = [self.year, movie2.year, movie3.year, movie4.year, movie5.year, movie6.year, movie7.year, movie8.year,movie9.year,movie10.year]
        movieyears.sort()
        for i in movieyears:
            if i == self.year:
                movieyears[i] = self.name
            
        movieyears[self.year] = self.name
        return(movieyears)

    def search_genre(self):
        pass

    def search_direct(self):
        pass

    def search_cast(self):
        pass

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



print(m1.sort_alpha(m2,m3,m4,m5,m6,m7,m8,m9,m10))
print(m1.sort_crono(m2,m3,m4,m5,m6,m7,m8,m9,m10))