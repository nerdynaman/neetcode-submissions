class TimeMap:
    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key] = self.data.get(key, {})
        self.data[key][timestamp] = value
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""
        timestamps = list(self.data[key].keys())
        low, high = 0, len(timestamps)-1
        # if timestamps[high] < timestamp:
        #     return ''

        maxTimestamp = float('-inf')
        
        while low<=high :
            mid = low + (high-low)//2

            if timestamps[mid] == timestamp:
                maxTimestamp = timestamps[mid] 
                break

            if timestamps[mid] > timestamp:
                high = mid - 1
            else:
                maxTimestamp = max(maxTimestamp, timestamps[mid])
                low = mid+1


        return self.data[key][maxTimestamp] if maxTimestamp>=0 else ""