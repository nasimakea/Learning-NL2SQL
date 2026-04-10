from src.pipeline.chat_pipeline import ChatPipeline

def main():
    print("🤖 NL2SQL Assistant (CLI)")
    print("Type 'exit' to quit\n")

    pipeline = ChatPipeline()

    while True:
        question = input("🧑 Ask: ")

        if question.lower() in ["exit", "quit"]:
            print("👋 Exiting...")
            break

        response = pipeline.run(question)

        if response["status"] == "success":
            print("\n📊 SQL Query:")
            print(response["query"])

            print("\n📈 Result:")
            for row in response["result"]["rows"]:
                print(row)

        elif response["status"] == "text_only":
            print("\n💬 Response:")
            print(response["message"])

        else:
            print("\n❌ Error:")
            print(response["error"])

        print("\n" + "-"*50 + "\n")


if __name__ == "__main__":
    main()