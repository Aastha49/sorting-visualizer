import tkinter as tk
from tkinter import ttk
import random
import time
import threading

class SortingVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Sorting Visualizer")
        self.root.geometry("1000x600")
        self.root.config(bg='white')

        self.data = []
        self.sorting = False
        self.speed = 0.1

        # UI Frame
        self.ui_frame = tk.Frame(self.root, bg='lightgray', padx=10, pady=5)
        self.ui_frame.pack(fill=tk.X)

        tk.Label(self.ui_frame, text="Array Size:", bg='lightgray').pack(side=tk.LEFT)
        self.size_entry = tk.Entry(self.ui_frame, width=5)
        self.size_entry.insert(0, "50")
        self.size_entry.pack(side=tk.LEFT, padx=5)

        self.algo_menu = ttk.Combobox(self.ui_frame, values=["Bubble", "Selection", "Insertion", "Merge", "Quick", "Heap"])
        self.algo_menu.current(0)
        self.algo_menu.pack(side=tk.LEFT, padx=5)

        self.speed_menu = ttk.Combobox(self.ui_frame, values=["Slow", "Medium", "Fast"])
        self.speed_menu.current(1)
        self.speed_menu.pack(side=tk.LEFT, padx=5)

        self.sort_btn = tk.Button(self.ui_frame, text="Sort", command=self.start_sorting_thread)
        self.sort_btn.pack(side=tk.LEFT, padx=5)

        self.new_array_btn = tk.Button(self.ui_frame, text="New Array", command=self.generate_array)
        self.new_array_btn.pack(side=tk.LEFT, padx=5)

        self.stop_btn = tk.Button(self.ui_frame, text="Stop", command=self.stop_sorting)
        self.stop_btn.pack(side=tk.LEFT, padx=5)

        self.canvas = tk.Canvas(self.root, bg='white', height=460)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.generate_array()

    def generate_array(self):
        self.sorting = False
        try:
            size = int(self.size_entry.get())
            size = max(5, min(size, 200))
        except ValueError:
            size = 50
            self.size_entry.delete(0, tk.END)
            self.size_entry.insert(0, "50")

        self.data = [random.randint(10, 400) for _ in range(size)]
        self.draw_array(self.data, ['skyblue'] * len(self.data))

    def draw_array(self, data, color_array):
        self.canvas.delete("all")
        c_width = self.canvas.winfo_width()
        c_height = self.canvas.winfo_height()
        x_width = c_width / max(len(data), 1)
        for i, height in enumerate(data):
            x0 = i * x_width
            y0 = c_height - height
            x1 = x0 + x_width
            y1 = c_height
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color_array[i])
            if len(data) <= 60:
                self.canvas.create_text(x0 + 2, y0, anchor=tk.SW, text=str(data[i]), font=("Arial", 8))
        self.root.update_idletasks()

    def set_speed(self):
        speed = self.speed_menu.get()
        return {"Slow": 0.3, "Medium": 0.1, "Fast": 0.01}.get(speed, 0.1)

    def start_sorting_thread(self):
        thread = threading.Thread(target=self.start_sorting, daemon=True)
        thread.start()

    def start_sorting(self):
        if not self.data:
            return
        self.sorting = True
        self.speed = self.set_speed()
        algorithm = self.algo_menu.get()
        self.disable_buttons()

        if algorithm == "Bubble":
            self.bubble_sort()
        elif algorithm == "Selection":
            self.selection_sort()
        elif algorithm == "Insertion":
            self.insertion_sort()
        elif algorithm == "Merge":
            self.merge_sort(0, len(self.data) - 1)
        elif algorithm == "Quick":
            self.quick_sort(0, len(self.data) - 1)
        elif algorithm == "Heap":
            self.heap_sort()

        self.draw_array(self.data, ['green'] * len(self.data))
        self.enable_buttons()

    def stop_sorting(self):
        self.sorting = False
        self.enable_buttons()

    def disable_buttons(self):
        self.sort_btn.config(state=tk.DISABLED)
        self.new_array_btn.config(state=tk.DISABLED)
        self.stop_btn.config(state=tk.NORMAL)

    def enable_buttons(self):
        self.sort_btn.config(state=tk.NORMAL)
        self.new_array_btn.config(state=tk.NORMAL)
        self.stop_btn.config(state=tk.DISABLED)

    # --- Sorting Algorithms ---

    def bubble_sort(self):
        for i in range(len(self.data) - 1):
            for j in range(len(self.data) - i - 1):
                if not self.sorting:
                    return
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
                self.draw_array(self.data, ['red' if x == j or x == j + 1 else 'skyblue' for x in range(len(self.data))])
                time.sleep(self.speed)

    def selection_sort(self):
        for i in range(len(self.data)):
            min_idx = i
            for j in range(i + 1, len(self.data)):
                if not self.sorting:
                    return
                if self.data[j] < self.data[min_idx]:
                    min_idx = j
                self.draw_array(self.data, ['red' if x == j or x == min_idx else 'skyblue' for x in range(len(self.data))])
                time.sleep(self.speed)
            self.data[i], self.data[min_idx] = self.data[min_idx], self.data[i]

    def insertion_sort(self):
        for i in range(1, len(self.data)):
            key = self.data[i]
            j = i - 1
            while j >= 0 and self.data[j] > key:
                if not self.sorting:
                    return
                self.data[j + 1] = self.data[j]
                j -= 1
                self.draw_array(self.data, ['red' if x == j or x == i else 'skyblue' for x in range(len(self.data))])
                time.sleep(self.speed)
            self.data[j + 1] = key

    def merge_sort(self, left, right):
        if not self.sorting:
            return
        if left < right:
            mid = (left + right) // 2
            self.merge_sort(left, mid)
            self.merge_sort(mid + 1, right)
            self.merge(left, mid, right)

    def merge(self, left, mid, right):
        left_part = self.data[left:mid + 1]
        right_part = self.data[mid + 1:right + 1]
        i = j = 0
        k = left
        while i < len(left_part) and j < len(right_part):
            if not self.sorting:
                return
            if left_part[i] <= right_part[j]:
                self.data[k] = left_part[i]
                i += 1
            else:
                self.data[k] = right_part[j]
                j += 1
            k += 1
            self.draw_array(self.data, ['purple' if x >= left and x <= right else 'skyblue' for x in range(len(self.data))])
            time.sleep(self.speed)
        while i < len(left_part):
            self.data[k] = left_part[i]
            i += 1
            k += 1
            self.draw_array(self.data, ['purple' if x >= left and x <= right else 'skyblue' for x in range(len(self.data))])
            time.sleep(self.speed)
        while j < len(right_part):
            self.data[k] = right_part[j]
            j += 1
            k += 1
            self.draw_array(self.data, ['purple' if x >= left and x <= right else 'skyblue' for x in range(len(self.data))])
            time.sleep(self.speed)

    def quick_sort(self, low, high):
        if not self.sorting:
            return
        if low < high:
            pi = self.partition(low, high)
            self.quick_sort(low, pi - 1)
            self.quick_sort(pi + 1, high)

    def partition(self, low, high):
        pivot = self.data[high]
        i = low - 1
        for j in range(low, high):
            if not self.sorting:
                return
            if self.data[j] <= pivot:
                i += 1
                self.data[i], self.data[j] = self.data[j], self.data[i]
            self.draw_array(self.data, ['red' if x == j or x == i else 'skyblue' for x in range(len(self.data))])
            time.sleep(self.speed)
        self.data[i + 1], self.data[high] = self.data[high], self.data[i + 1]
        return i + 1

    def heap_sort(self):
        n = len(self.data)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(n, i)
        for i in range(n - 1, 0, -1):
            self.data[i], self.data[0] = self.data[0], self.data[i]
            self.heapify(i, 0)
            self.draw_array(self.data, ['red' if x == i or x == 0 else 'skyblue' for x in range(len(self.data))])
            time.sleep(self.speed)

    def heapify(self, n, i):
        if not self.sorting:
            return
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and self.data[l] > self.data[largest]:
            largest = l
        if r < n and self.data[r] > self.data[largest]:
            largest = r
        if largest != i:
            self.data[i], self.data[largest] = self.data[largest], self.data[i]
            self.heapify(n, largest)

# --- Run ---
if __name__ == "__main__":
    root = tk.Tk()
    app = SortingVisualizer(root)
    root.mainloop()
