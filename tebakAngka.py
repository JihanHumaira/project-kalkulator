import random

print("------------------------------")
print("     M&M guessing game!")
print("------------------------------")
print("Guess the number of M&Ms and you get lunch on the house!")
print()

mm_count = random.randint(1, 5)
attempt_limit = 5
attempts = 0

while attempts < attempt_limit:
    guess_text = input("How many M&Ms are in the jar? ")
    try:
        guess = int(guess_text)
    except:
        print("❗ masukkan angka 1 - 5")
        continue  # kembali ke awal loop (jangan hitung attempt)

    if guess < 1 or guess > 5:
        print("❗ masukkan angka 1 - 5")
        continue

    attempts += 1

    if mm_count == guess:
        print(f"You got a free lunch! It was {guess}.")
        break
    elif guess < mm_count:
        print("Sorry, that's too LOW!")
        print(f"your remaining attemps left:{attempt_limit-attempts} ")
    else:
        print("That's too HIGH!")
        print(f"your remaining attemps left:{attempt_limit-attempts} ")

print(f"Bye, you're done in {attempts}!")