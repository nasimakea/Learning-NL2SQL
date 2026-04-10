# setup_database.py

from database.db_setup import create_tables


def main():
    print("🚀 Setting up database...")
    create_tables()
    print("✅ Database setup completed!")


if __name__ == "__main__":
    main()