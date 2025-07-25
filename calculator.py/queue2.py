class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def size(self):
        return len(self.items)

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

def main():
    q = Queue()
    while True:
        print("\nQueue Operations:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Size")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            item = input("Enter item to enqueue: ")
            q.enqueue(item)
            print("Enqueued:", item)
        elif choice == '2':
            item = q.dequeue()
            if item is None:
                print("Queue is empty")
            else:
                print("Dequeued:", item)
        elif choice == '3':
            item = q.peek()
            if item is None:
                print("Queue is empty")
            else:
                print("Front item:", item)
        elif choice == '4':
            print("Queue size:", q.size())
        elif choice == '5':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
