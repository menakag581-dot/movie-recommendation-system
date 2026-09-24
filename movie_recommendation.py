import csv

# Read movie data
movies = []

with open("movies.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        movies.append(row)


# Get movie name from user
movie_name = input("Enter a movie name: ")

# Find the selected movie
selected_movie = None

for movie in movies:
    if movie["title"].lower() == movie_name.lower():
        selected_movie = movie
        break


# Recommend similar movies
if selected_movie:

    print("\nMovies you may like:\n")

    selected_genre = selected_movie["genre"]
    selected_keywords = selected_movie["keywords"].split()

    recommendations = []

    for movie in movies:
        if movie["title"].lower() == movie_name.lower():
            continue

        score = 0

        if movie["genre"] == selected_genre:
            score += 2

        movie_keywords = movie["keywords"].split()

        for keyword in selected_keywords:
            if keyword in movie_keywords:
                score += 1

        recommendations.append((score, movie["title"]))


    # Sort by similarity score
    recommendations.sort(reverse=True)

    # Display top 5 recommendations
    for score, title in recommendations[:5]:
        print("-", title)

else:
    print("\nMovie not found.")
    print("Please enter a movie name from the dataset.")
