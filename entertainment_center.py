import media
import fresh_tomatoes
"""Submit values for Toy Story Movie"""
toy_story = media.Movie(
    "Toy Story 2",
    "Toys Come to Life",
    "https://upload.wikimedia.org/wikipedia/en/c/c0/Toy_Story_2.jpg",
    "https://www.youtube.com/watch?v=Lu0sotERXhI")
"""Submit values for Avatar movie"""
avatar = media.Movie(
    "Avatar",
    "A marine on an alien planet",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https: // www.youtube.com/watch?v=5PSNL1qE6VY")
"""Submit values for School of Rock Movie"""
school_of_rock = media.Movie(
    "School of Rock",
    "Story of a rock band",
    "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
    "https://youtu.be/5afGGGsxvEA")
"""Submit values for Ratatouille Movie"""
ratatouille = media.Movie(
    "Ratatouille",
    "Movie of a mouse",
    "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
    "https://youtu.be/fIjHfW6y4Mg")

movies = [toy_story, avatar, school_of_rock, ratatouille]
fresh_tomatoes.open_movies_page(movies)
