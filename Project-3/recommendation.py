
# AI Recommendation Logic
# DecodeLabs Internship - Project 3

# Movie database with genres
movies = [
    {"title": "The Dark Knight", "genres": ["action", "crime", "drama"]},
    {"title": "Avengers: Endgame", "genres": ["action", "sci-fi", "adventure"]},
    {"title": "The Hangover", "genres": ["comedy"]},
    {"title": "The Pursuit of Happyness", "genres": ["drama", "inspirational"]},
    {"title": "Interstellar", "genres": ["sci-fi", "adventure", "drama"]},
    {"title": "The Conjuring", "genres": ["horror", "thriller"]},
    {"title": "Toy Story", "genres": ["animation", "comedy", "family"]},
    {"title": "John Wick", "genres": ["action", "thriller"]},
    {"title": "The Notebook", "genres": ["romance", "drama"]},
    {"title": "Finding Nemo", "genres": ["animation", "adventure", "family"]},
]

print("=" * 45)
print("       AI MOVIE RECOMMENDATION SYSTEM")
print("=" * 45)

print("\nAvailable genres:")
print("Action, Comedy, Drama, Sci-Fi, Horror,")
print("Thriller, Romance, Animation, Adventure,")
print("Family, Crime, Inspirational")

user_input = input(
    "\nEnter your favorite genres separated by commas: "
).lower()

# Convert the input into a set of preferences
preferences = {
    genre.strip()
    for genre in user_input.split(",")
    if genre.strip()
}

if not preferences:
    print("\nPlease enter at least one genre.")
else:
    # Match user preferences with movie genres
    recommendations = []

    for movie in movies:
        matching_genres = preferences.intersection(movie["genres"])

        if matching_genres:
            recommendations.append(
                (movie["title"], matching_genres)
            )

    # Show the movies with the most matching genres first
    recommendations.sort(
        key=lambda item: len(item[1]),
        reverse=True
    )

    print("\nRecommended movies for you:")

    if recommendations:
        for title, matched_genres in recommendations:
            print(
                f"- {title} "
                f"(Matched: {', '.join(sorted(matched_genres))})"
            )
    else:
        print("No matches found. Try another genre.")

print("\nThank you for using the recommendation system!")
