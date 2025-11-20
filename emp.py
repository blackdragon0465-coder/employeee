import sys

if len(sys.argv) != 3:
    print("Usage: python student.py <name> <id> <salary>")
    sys.exit(1)

script_name = sys.argv[0]
name = sys.argv[1]
id = sys.argv[2]
salary = sys.argv[3]

print("Script Name:", script_name)
print("Name:", name)
print("ID Number:", id)
print("Salary:", salary)