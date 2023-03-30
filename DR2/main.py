st = input("Enter string: ");

vowels = "аеєиіїоуюя";

result = "";

for letter in vowels:
    if letter in list(set(st)):
        result = result + letter;

print(f"Result: {result}");
