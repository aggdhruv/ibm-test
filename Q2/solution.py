
class Record:
    def __init__(self, num, valid, error_code="true"):
        self.num = num
        self.isValid = valid
        self.error_code = error_code


n = int(input())
records = []

for i in range(n):
    line = input().split()
    if line[1] == "false":
        sample = Record(int(line[0]), line[1], line[2])
    else:
        sample = Record(int(line[0]), line[1])
    records.append(sample)


allValid = "true"
errorCodes = []
for record in records:
    if record.isValid == "false":
        allValid = "false"
        errorCodes.append(record.error_code)

if allValid == "true":
    print("Yes")
else:
    print("No")
    print(" ".join(errorCodes))