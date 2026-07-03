from processor import FileProcessor

procesor=FileProcessor("sample.txt")

procesor.write("Hello")
# print(procesor.read())
procesor.append(" world")
print(procesor.read())