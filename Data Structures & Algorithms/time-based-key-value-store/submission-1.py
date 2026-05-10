class TimeMap:

    def __init__(self):
        self.time_map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.time_map:
            self.time_map[key].append([value, timestamp])
        else:
            self.time_map[key] = [[value, timestamp]]
        

    def get(self, key: str, timestamp: int) -> str:
        if key in self.time_map:
            L = 0
            R = len(self.time_map[key]) - 1
            message = ""
            while L <= R:
                mid = (L + R) // 2
                if self.time_map[key][mid][1] > timestamp:
                    R = mid - 1
                elif self.time_map[key][mid][1] < timestamp:
                    message = self.time_map[key][mid][0]
                    L = mid + 1
                else:
                    return self.time_map[key][mid][0]
            return message
        else:
            return ""
        
