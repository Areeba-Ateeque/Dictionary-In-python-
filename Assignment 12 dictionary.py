#1:Word Counter:
# Write a program that reads a sentence and counts the number of times each word appears. Use 
#a dictionary to store the word counts.
def word_counter(sentence):
    # Convert the sentence to lowercase to ensure case-insensitive counting
    words = sentence.lower().split()
    
    word_counts = {}
    
    for word in words:
        # Remove punctuation if needed
        word = word.strip('.,!?()[]{}"\'')
        
        # Increment the count for each word
        word_counts[word] = word_counts.get(word, 0) + 1
    
    return word_counts

# Example usage:
sentence = input("Enter a sentence: ")
result = word_counter(sentence)
# Display the word counts
for word, count in result.items():
    print(f"{word}: {count}")
    
#2:Grade Calculator:
# Create a program that asks the user for their scores in different subjects and calculates their 
#overall grade based on a grading scale stored in a dictionary
def calculate_grade(scores):
    grading_scale = {
        "A+": (90, 100),
        "A": (80, 89),
        "B+": (70, 79),
        "B": (60, 69),
        "C": (50, 59),
        "F": (0, 49)
    }
    
    total_score = sum(scores)
    average_score = total_score / len(scores)
    
    for grade, (lower_bound, upper_bound) in grading_scale.items():
        if lower_bound <= average_score <= upper_bound:
            return grade
    
    return "F"

# Example usage
subject_scores = [85, 92, 78, 70, 60]
overall_grade = calculate_grade(subject_scores)
print("Overall Grade:", overall_grade)
#3
#Develop a program that allows users to add, remove, and check off items on a shopping list 
#stored in a dictionary.
# Shopping list dictionary
# Shopping list dictionary
shopping_list = {}

def add_item(item, quantity):
    shopping_list[item] = quantity
    print(item, "has been added to the shopping list.")

def remove_item(item):
    if item in shopping_list:
        del shopping_list[item]
        print(item, "has been removed from the shopping list.")
    else:
        print(item, "is not in the shopping list.")

def check_off_item(item):
    if item in shopping_list:
        print(item, "has been checked off.")
    else:
        print(item, "is not in the shopping list.")

# Example usage
add_item("Apples", 5)
add_item("Bananas", 3)
check_off_item("Apples")
remove_item("Bananas")
##4
 #Movie Rating Tracker:
# Design a program that lets users rate movies on a scale from 1 to 5. Use a dictionary to store 
#movie titles and their average ratings.
movies = {}
def rate_movie():
    title = input("Enter the movie title: ")
    rating = int(input("Enter your rating (1-5): "))
    
    movies[title] = rating

def calculate_average_rating():
    total_rating = 0
    num_ratings = 0
    # Iterate through the dictionary
    for rating in movies.values():
        total_rating += rating
        num_ratings += 1
    # Check for division by zero
    if num_ratings == 0:
        return 0
    # Calculate the average rating
    average_rating = total_rating / num_ratings
    return average_rating

# Function to display average rating for a movie
def display_average_rating():
    title = input("Enter the movie title: ")
    average_rating = calculate_average_rating()
    if average_rating:
        print(f"The overall average rating is {average_rating}.")
    else:
        print("No ratings available.")

# Test the program
rate_movie()
rate_movie()
average = calculate_average_rating()
print(f"The overall average rating is {average}.")
display_average_rating()

#5
#Temperature Converter:
# Build a program that converts temperatures between Celsius and Fahrenheit using a dictionary 
#to store conversion factors.
def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def temperature_converter():
    conversion_factors = {
        'celsius_to_fahrenheit': celsius_to_fahrenheit,
        'fahrenheit_to_celsius': fahrenheit_to_celsius
    }

    conversion_type = input("Choose conversion type (celsius_to_fahrenheit or fahrenheit_to_celsius): ")

    if conversion_type in conversion_factors:
        temperature_value = float(input(f"Enter temperature in {conversion_type.split('_')[0]}: "))
        converted_temperature = conversion_factors[conversion_type](temperature_value)
        print(f"The converted temperature is: {converted_temperature} {conversion_type.split('_')[1]}")
    else:
        print("Invalid conversion type. Please choose celsius_to_fahrenheit or fahrenheit_to_celsius.")

# Example usage:
temperature_converter()

    