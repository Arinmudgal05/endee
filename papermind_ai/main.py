
from backend.rag_pipeline import ask_question

def main():
    print("PaperMind AI - Research Paper Assistant")
    print("Type 'exit' to quit\n")

    while True:
        query = input("Ask a question about the paper: ")

        if query.lower() == "exit":
            break

        answer = ask_question(query)
        print("\nAnswer:", answer)
        print("\n---------------------\n")

if __name__ == "__main__":
    main()
