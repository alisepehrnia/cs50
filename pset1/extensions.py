file_formats = [("gif", "image/gif"), ("jpg", "image/jpeg"), ("jpeg", "image/jpeg")]

inp = input("Enter your file name (full with . extension at end): ")
extension = inp.lower().split(".")[-1]

output = "application/octet-stream"

for file_format in file_formats:
    format, mime = file_format
    if format == extension:
        output = mime

print(output)