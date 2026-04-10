from src.pipeline.chat_pipeline import ChatPipeline
def main():
    pipeline = ChatPipeline()
    
    response = pipeline.run("How many patients do we have?")
    print(response)

if __name__ == "__main__":
    main()