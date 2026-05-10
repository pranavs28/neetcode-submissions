class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for op in operations:
            if op == '+':
                record.append(record[-1] + record[-2])
                pass
            elif op == 'D':
                record.append(record[-1] * 2)
                pass
            elif op == 'C':
                record.pop()
                pass
            else:
                record.append(int(op))
        return sum(record)

 