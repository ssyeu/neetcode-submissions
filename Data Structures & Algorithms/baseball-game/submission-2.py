class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for num in operations:
            if num == "+":
                record.append(record[-1] + record[-2])
            elif num == "D":
                record.append(2 * record[-1])
            elif num == "C":
                record.pop()
            else:
                record.append(int(num))
        return sum(record)
