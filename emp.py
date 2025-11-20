import sys

if len(sys.argv) != 5:
    print("Usage: python emp.py <name> <id> <salary> <experiance>")
    sys.exit(1)

script_name = sys.argv[0]
name = sys.argv[1]
id = sys.argv[2]
salary = sys.argv[3]
experiance = sys.argv[4]

print("Script Name:", script_name)
print("Name:", name)
print("ID Number:", id)
print("Salary:", salary)
print("Experiance:", experiance)
