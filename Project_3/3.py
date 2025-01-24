import tkinter as tk
from tkinter import messagebox, ttk
from ttkbootstrap import Style
from quiz_data import quiz_data

# Function to start the quiz
def start_quiz():
    global user_name, user_email, user_college_year, user_number, user_address
    user_name = name_entry.get()
    user_email = email_entry.get()
    user_college_year = college_year_entry.get()
    user_number = number_entry.get()
    user_address = address_entry.get()

    if not user_name or not user_email or not user_college_year or not user_number or not user_address:
        messagebox.showwarning("Input Error", "Please enter all the details.")
        return

    # Hide the user info frame and show the quiz frame
    user_info_frame.pack_forget()
    quiz_frame.pack(fill="both", expand=True)
    show_question()
    start_timer()

# Function to display the current question and choices
def show_question():
    # Get the current question from the quiz_data list
    question = quiz_data[current_question]
    qs_label.config(text=question["question"])

    # Display the choices on the buttons
    choices = question["choices"]
    for i in range(4):
        choice_btns[i].config(text=choices[i], state="normal")  # Reset button state

    # Clear the feedback label and disable the next button
    feedback_label.config(text="")
    next_btn.config(state="disabled")

    # Reset the border color
    root.config(bg=style.lookup('TFrame', 'background'))

# Function to check the selected answer and provide feedback
def check_answer(choice):
    # Get the current question from the quiz_data list
    question = quiz_data[current_question]
    selected_choice = choice_btns[choice].cget("text")

    # Check if the selected choice matches the correct answer
    if selected_choice == question["answer"]:
        # Update the score and display it
        global score
        score += 1
        score_label.config(text="Score: {}/{}".format(score, len(quiz_data)))
        feedback_label.config(text="Correct!", foreground="green")
        root.config(bg="green")
    else:
        feedback_label.config(text="Incorrect!", foreground="red")
        root.config(bg="red")
    
    # Disable all choice buttons and enable the next button
    for button in choice_btns:
        button.config(state="disabled")
    next_btn.config(state="normal")

# Function to move to the next question
def next_question():
    global current_question
    current_question += 1

    if current_question < len(quiz_data):
        # If there are more questions, show the next question
        show_question()
    else:
        # If all questions have been answered, display the final score and end the quiz
        end_quiz()

# Function to end the quiz
def end_quiz():
    messagebox.showinfo("Quiz Completed",
                        "Quiz Completed! Final score: {}/{}".format(score, len(quiz_data)))
    root.destroy()

# Function to start the timer
def start_timer():
    global time_left
    time_left = 600  # 10 minutes in seconds
    update_timer()

# Function to update the timer display
def update_timer():
    global time_left
    minutes, seconds = divmod(time_left, 60)
    timer_label.config(text="Time left: {:02d}:{:02d}".format(minutes, seconds))
    if time_left > 0:
        time_left -= 1
        root.after(1000, update_timer)
    else:
        end_quiz()

# Create the main window
root = tk.Tk()
root.title("Quiz App")
root.geometry("800x800")
style = Style(theme="flatly")

# Configure the font size for the question and choice buttons
style.configure("TLabel", font=("Helvetica", 20))
style.configure("TButton", font=("Helvetica", 16))

# Create the user info frame
user_info_frame = ttk.Frame(root)
user_info_frame.pack(fill="both", expand=True, padx=20, pady=20)

# Welcome message
welcome_label = ttk.Label(user_info_frame, text="WELCOME to Ashvini Hirve's Project", font=("Helvetica", 24))
welcome_label.pack(pady=20)

# User details entry
def create_label_entry(parent, text):
    frame = ttk.Frame(parent)
    frame.pack(pady=5, fill="x")
    label = ttk.Label(frame, text=text, width=15, anchor="w")
    label.pack(side="left")
    entry = ttk.Entry(frame, font=("Helvetica", 16), width=30)
    entry.pack(side="left", padx=5)
    return entry

name_entry = create_label_entry(user_info_frame, "Name:")
email_entry = create_label_entry(user_info_frame, "Email:")
college_year_entry = create_label_entry(user_info_frame, "College Year:")
number_entry = create_label_entry(user_info_frame, "Phone Number:")
address_entry = create_label_entry(user_info_frame, "Address:")

# Quiz information
quiz_info_label = ttk.Label(user_info_frame, text="Quiz Information:\nTime: 10 minutes\nQuestions: 10\nArea: India", font=("Helvetica", 16))
quiz_info_label.pack(pady=20)

start_btn = ttk.Button(user_info_frame, text="Start Quiz", command=start_quiz, style="TButton", padding=10)
start_btn.pack(pady=20)

# Create the quiz frame
quiz_frame = ttk.Frame(root)

# Create the question label
qs_label = ttk.Label(
    quiz_frame,
    anchor="center",
    wraplength=700,
    padding=10
)
qs_label.pack(pady=10)

# Create the choice buttons
choice_btns = []
for i in range(4):
    button = ttk.Button(
        quiz_frame,
        command=lambda i=i: check_answer(i)
    )
    button.pack(pady=5)
    choice_btns.append(button)

# Create the feedback label
feedback_label = ttk.Label(
    quiz_frame,
    anchor="center",
    padding=10
)
feedback_label.pack(pady=10)

# Initialize the score
score = 0

# Create the score label
score_label = ttk.Label(
    quiz_frame,
    text="Score: 0/{}".format(len(quiz_data)),
    anchor="center",
    padding=10
)
score_label.pack(pady=10)

# Create the timer label
timer_label = ttk.Label(
    quiz_frame,
    text="Time left: 10:00",
    anchor="center",
    padding=10
)
timer_label.pack(pady=10)

# Create the next button
next_btn = ttk.Button(
    quiz_frame,
    text="Next",
    command=next_question,
    state="disabled",
    padding=10
)
next_btn.pack(pady=10)

# Initialize the current question index
current_question = 0

# Start the main event loop
root.mainloop()
