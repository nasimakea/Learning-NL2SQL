from src.components.memory import MyMemory   # adjust path if needed

def test_memory():
    try:
        print("🚀 Testing MyMemory...")

        # Initialize
        memory = MyMemory()

        print("✅ Memory initialized successfully!")

    except Exception as e:
        print("❌ Error occurred:", e)


if __name__ == "__main__":
    test_memory()