class TimeMap:

    def __init__(self):
        self.db = defaultdict(list)
    
    def _search(self, timestamp, lst):

        left, right = 0, len(lst)-1
        while left <= right:
            mid = (left+right)//2
            time_stamp, value = lst[mid]
            if time_stamp == timestamp:
                return value
            elif time_stamp > timestamp:
                right = mid - 1
            else:
                left = mid + 1
        
        return lst[right][1] if right >= 0 else ""

        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.db[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key in self.db:
            # do the complete binary search thing
            return self._search(timestamp, self.db[key])
        else:
            return ""

        
