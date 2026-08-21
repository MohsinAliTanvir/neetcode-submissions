class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:

        # Stack stores:
        # (start_index, height)
        #
        # start_index tells us how far left
        # this height can extend
        stack = []

        max_area = 0

        for i, height in enumerate(heights):

            # By default, this bar starts at its own index
            start = i

            # If current bar is shorter than the bar on top,
            # the taller bar cannot continue anymore
            while stack and stack[-1][1] > height:

                previous_start, previous_height = stack.pop()

                # Rectangle ends just before current index
                width = i - previous_start

                area = previous_height * width

                max_area = max(max_area, area)

                # Current shorter bar can extend backward
                # to where the taller popped bar started
                start = previous_start

            # Store current bar with the earliest place
            # it can start from
            stack.append((start, height))

        # Any bars still in stack were never blocked
        # by a shorter bar, so they can go to the end
        n = len(heights)

        while stack:

            start, height = stack.pop()

            width = n - start

            area = height * width

            max_area = max(max_area, area)

        return max_area
        