import random

# A list of sample quotes
sample_quotes = [
    "Life is what happens when you're busy making other plans. - John Lennon",
    "In three words I can sum up everything I've learned about life: it goes on. - Robert Frost",
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "You miss 100% of the shots you don't take. - Wayne Gretzky",
]

def get_random_quote():
    return random.choice(sample_quotes)

def main():
    print("Welcome to the Random Quote Generator!")
    while True:
        input("Press Enter to get a random quote...")
        quote = get_random_quote()
        print(f"\n{quote}\n")

if __name__ == "__main__":
    main()
