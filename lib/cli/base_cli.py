class BaseCLI:
    def __init__(self, session):
        self.session = session

    def input_int(self, prompt, allow_empty=False):
        while True:
            val = input(prompt).strip()
            if allow_empty and val == "":
                return ""  
            try:
                return int(val)  
            except ValueError:
                print("Please enter a valid number.")  


    def input_str(self, prompt, allow_empty=False):
        while True:
            val = input(prompt).strip()
            if val or allow_empty:
                return val
            print("Input cannot be empty.")

    def pause(self):
        input("\nPress Enter to continue...")

    def list_all(self):
        raise NotImplementedError()

    def create(self):
        raise NotImplementedError()
    
    def update(self):
        raise NotImplementedError()

    def delete(self):
        raise NotImplementedError()

    def find_by_attribute(self):
        raise NotImplementedError()

    def view_related(self):
        raise NotImplementedError()

    def menu(self):
        raise NotImplementedError()

    def run(self):
        while True:
            self.menu()
            choice = input("> ").strip()
            if choice == "0":
                break
            elif choice == "1":
                self.create()
            elif choice == "2":
                self.update()
            elif choice == "3":
                self.delete()
            elif choice == "4":
                self.list_all()
            elif choice == "5":
                self.find_by_attribute()
            elif choice == "6":
                self.view_related()
            else:
                print("Invalid choice. Try again.")
            self.pause()
