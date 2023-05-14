class Solution:
    def cascading(self, height: List[int]) -> int:
        total_water = 0

        prev_max_height = 0
        prev_water = 0
        for idx, curr_height in enumerate(height):
            if prev_max_height < curr_height:
                total_water += prev_water
                prev_max_height = curr_height
                prev_water = 0
            else:
                prev_water += prev_max_height - curr_height

        return total_water

    def flat(self, height: List[int]) -> int:
        max_height = max(height)
        first_max_height_idx = height.index(max_height)
        last_max_height_idx = - height[::-1].index(max_height) - 1

        water = 0
        for curr_height in height[first_max_height_idx:last_max_height_idx]:
            water += max_height - curr_height

        return water

    def trap(self, height: List[int]) -> int:
        cascading_water = self.cascading(height)
        descending_water = self.cascading(height[::-1])
        flat_water = self.flat(height)

        return cascading_water + descending_water + flat_water