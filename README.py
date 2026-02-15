# my_test_repository.py

class MyTestRepository:
    def __init__(self):
        self.description = "This is a simple repository used for testing the ingestion and processing flow."

    def display_info(self):
        print("My Test Repository")
        print(self.description)

if __name__ == "__main__":
    repo = MyTestRepository()
    repo.display_info()
