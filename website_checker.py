user_inp = input("Please enbter a website URL: ")

if user_inp.startswith("https://"):
    print("The URL is secure.")
elif user_inp.startswith("http://"):
    print("The URL is not secure.")
else:
    print("The UURL is inavlid")
