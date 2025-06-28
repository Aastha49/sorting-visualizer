🧮 Sorting Visualizer using Tkinter



This project is a Graphical Sorting Visualizer developed in Python using the Tkinter GUI library. It allows you to visualize popular sorting algorithms like Bubble Sort, Insertion Sort, Selection Sort, Merge Sort, Quick Sort, and Heap Sort in real-time.



📌 Features
User Interface: Intuitive GUI using Tkinter.

Algorithms Supported:

Bubble Sort

Selection Sort

Insertion Sort

Merge Sort

Quick Sort

Heap Sort

Speed Control: Choose from Slow, Medium, or Fast.

Dynamic Array: Easily generate a new random array of configurable size.

Threading: Sorting runs in a separate thread to keep the GUI responsive.

Live Visualization: Color-coded animation of the sorting process.



🖥️ Tech Stack
Python 3

Tkinter (for GUI)

Threading (for smooth sorting animation)

Random (for array generation)

Time (for animation delays)



🧑‍💻 How to Run
Clone the Repository

bash
Copy
Edit
git clone https://github.com/yourusername/sorting-visualizer-tkinter.git
cd sorting-visualizer-tkinter
Run the Script
Make sure you have Python 3 installed. Then run:

bash
Copy
Edit
python sorting_visualizer.py



📸 UI Overview
Array Size Input: Enter number of elements (between 5 and 200).

Algorithm Dropdown: Choose your preferred sorting algorithm.

Speed Dropdown: Set the speed of animation.

Sort Button: Start sorting the array.

New Array: Generate a fresh random array.

Stop: Halt the current sorting process.



🎨 Visual Cues
🔵 Sky Blue - Unsorted array

🔴 Red - Elements being compared or swapped

🟣 Purple - Elements in active merge region

🟢 Green - Final sorted array



🚧 Limitations
UI responsiveness depends on thread timing and user machine performance.

Visualization becomes harder to read with very large arrays (>100).



🙌 Contributions
Feel free to fork this repository and submit pull requests for enhancements like:

Adding more sorting algorithms

Improving visual themes

Adding sound effects

Exporting step-by-step GIFs


