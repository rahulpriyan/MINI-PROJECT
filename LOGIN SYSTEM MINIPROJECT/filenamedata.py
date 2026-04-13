try:
    filename = input("Enter file name: ")
    data = input("Enter text: ")

    if filename == "":
        raise Exception("File name cannot be empty")

    f = open(filename, "w")
    f.write(data)

    print("Data written successfully")

except Exception as e:
    print("Error:", e)

finally:
    # This block usually contains cleanup code, like closing the file
    try:
        f.close()
    except NameError:
        # If 'f' was never defined because opening failed, ignore the error
        pass