class MaxHeap:
    def __init__(self):
        self.heap = []
        # Initializes an Empty List to Represent the Heap

    def insert(self, val):
        self.heap.append(val)
        # Adds the New Value to the End of the Heap
        self._heapify_up(len(self.heap) - 1)
        # Restores the max-heap Property by Moving the New Value up the Heap

    def delete(self, val):
        try:
            index = self.heap.index(val)
            # Finds the Index of the Value to be Deleted
            self.heap[index] = self.heap[-1]
            # Replaces the Value to be Deleted with the Last Element
            self.heap.pop()
            # Removes the Last Element
            if index < len(self.heap):
                self._heapify_down(index)
                # Restores the max-heap Property by Moving the New Value down the Heap
                self._heapify_up(index)
                # Ensures the New Value is in the Correct Position
            return val
            # Returns the Deleted Value
        except ValueError:
            return None
            # Returns None if the Value is Not Found

    def get_max(self):
        if len(self.heap) > 0:
            return self.heap[0]
            # Returns the Maximum Value (the Root of the Heap)
        return None
        # Returns None if the Heap is Empty

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = (
                self.heap[parent_index],
                self.heap[index],
            )
            # Swaps the Current Value with its Parent if the Current Value is Greater
            self._heapify_up(parent_index)
            # Recursively calls heapify up on the Parent Index

    def _heapify_down(self, index):
        largest = index
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2

        if (
            left_child_index < len(self.heap)
            and self.heap[left_child_index] > self.heap[largest]
        ):
            largest = left_child_index
            # Updates Largest to Left Child if Left Child is Greater than Current Largest
        if (
            right_child_index < len(self.heap)
            and self.heap[right_child_index] > self.heap[largest]
        ):
            largest = right_child_index
            # Updates Largest to Right Child if Right Child is Greater than Current Largest

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            # Swaps the Current Value with the Largest Child if needed
            self._heapify_down(largest)
            # Recursively calls heapify down on the Largest Index


def menu():
    max_heap = MaxHeap()
    # Creates an Instance of the MaxHeap Class
    while True:
        print("\nMax Heap Operations:")
        print("1. Insert")
        print("2. Delete")
        print("3. Get Max")
        print("4. Exit")

        choice = int(input("Enter Your Choice: "))
        # Prompts the user to Enter a Choice

        if choice == 1:
            value = int(input("Enter Value to Insert: "))
            max_heap.insert(value)
            # Inserts the Entered Value into the Heap
            print(f"Inserted {value} into the Heap.")
        elif choice == 2:
            value = int(input("Enter Value to Delete: "))
            deleted_value = max_heap.delete(value)
            # Deletes the Entered Value from the Heap
            if deleted_value is not None:
                print(f"Deleted {value} from the Heap.")
            else:
                print("Value Not Found in the Heap.")
        elif choice == 3:
            max_value = max_heap.get_max()
            # Gets the Maximum Value from the Heap
            if max_value is not None:
                print(f"Max Value in the Heap is {max_value}.")
            else:
                print("Heap is Empty.")
        elif choice == 4:
            print("Thank You")
            break
            # Exits the Menu
        else:
            print("Invalid Input")
            # Handles Invalid Input


if __name__ == "__main__":
    menu()
    # Runs the menu Function when the Script is Executed
