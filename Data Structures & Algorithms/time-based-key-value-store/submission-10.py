class TimeMap:
    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key] = self.data.get(key, [])
        self.data[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""
        timestamps = self.data[key]
        low, high = 0, len(timestamps)-1
        # if timestamps[high] < timestamp:
        #     return ''

        maxTimestamp = float('-inf')
        
        while low<=high :
            mid = low + (high-low)//2

            if timestamps[mid][0] == timestamp:
                maxTimestamp = mid
                break

            if timestamps[mid][0] > timestamp:
                high = mid - 1
            else:
                maxTimestamp = max(maxTimestamp, mid)
                low = mid+1


        return self.data[key][maxTimestamp][1] if maxTimestamp>=0 else ""