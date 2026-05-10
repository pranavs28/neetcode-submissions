class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        total = 0
        for op in operations:
            if op == '+':
                total += (record[-1] + record[-2])
                record.append(record[-1] + record[-2])
                pass
            elif op == 'D':
                total += (record[-1] * 2)
                record.append(record[-1] * 2)
                pass
            elif op == 'C':
                total = total - record[-1]
                record.pop()
                pass
            else:
                total += int(op)
                record.append(int(op))
        return total

 