# AI Movie Recommendation System

## DecodeLabs AI Internship — Project 3

### Overview
This project is a simple content-based movie recommendation system developed using Python. It recommends movies based on the user's favorite genres by matching their preferences with movie genre information.

### Project Objectives
- Accept user interests as input.
- Match user preferences with movie genres.
- Recommend relevant movies.
- Rank recommendations by the number of matching genres.
- Handle inputs that produce no matches.

### Features
- Supports multiple genre preferences.
- Matches genres without requiring uppercase or lowercase input consistency.
- Displays the genres matched for each recommendation.
- Shows a helpful message when no matching movies are found.

### Technologies Used
- Python
- Lists and dictionaries
- Sets and set intersection
- Conditional statements
- Loops and sorting

### How to Run
1. Install Python.
2. Open a terminal in the project directory.
3. Run:

```bash
python recommendation.py
```

4. Enter your favorite genres separated by commas, for example:

```text
action, sci-fi
```

### Example Output

```text
Recommended movies for you:
- Avengers: Endgame (Matched: action, sci-fi)
- The Dark Knight (Matched: action)
- Interstellar (Matched: sci-fi)
- John Wick (Matched: action)
```

### How It Works
The program stores a small collection of movies and their genres. It compares the user's selected genres with each movie's genres and ranks matching movies by the number of shared genres.

### Learning Outcomes
- User input handling
- Preference matching
- Basic recommendation logic
- Set operations and pattern matching
- Sorting and displaying results

### Project Information
**Internship:** DecodeLabs Artificial Intelligence Internship  
**Project:** Project 3 — AI Recommendation Logic
