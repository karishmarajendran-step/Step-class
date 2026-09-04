def validate_file_extension(filename):
    dot_position = filename.rfind(".")

    if dot_position == -1:
        return "Rejected — invalid file type"

    extension = filename[dot_position + 1:]

    if extension.lower() in ["pdf", "docx", "zip"]:
        return "Accepted"

    return "Rejected — invalid file type"


filename = input("Enter filename: ")

print(validate_file_extension(filename))