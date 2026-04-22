# Number-guessing-game
A number guessing game created by python Tkinder

# Mind-Reading Number Guesser

A sleek, interactive GUI application built with Python and Tkinter. This isn't just a simple guessing game; it features a simulated "mind-reading" process using multi-threading to ensure a smooth user experience without freezing the interface.

# Key Features

Multithreaded Execution: Uses the threading module to run heavy "brainwave analysis" simulations in the background, keeping the GUI responsive.
Dynamic UI: Features a custom progress bar with real-time status updates and a custom-themed background.
Error Handling: Robust validation for user inputs (non-integers, empty strings, and out-of-range numbers).
Asset Integration: Demonstrates implementation of custom icons and background images within a Tkinter environment.
# Tech Stack
Language: Python 3.x
Library: Tkinter (GUI)
Concurrency: Threading
Styling: Custom assets (Images/Icons)
How It Works (The Logic)
Input Validation: The app checks if the input is a valid integer between 1 and 100.
The "Mind Reading" Simulation: A secondary thread is spawned to handle the Progressbar. This prevents the main mainloop() from hanging while the "Analyzing Brainwaves" loop runs.
Result: The app compares your guess against a randomly generated number and provides feedback via messagebox.
# Future Improvements
[ ] Add a "High Score" system using a local SQLite database.
[ ] Implement difficulty levels (Easy, Medium, Hard).
[ ] Create a standalone executable (.exe) using PyInstaller.
