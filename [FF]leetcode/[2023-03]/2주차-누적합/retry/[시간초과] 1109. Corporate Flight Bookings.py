from typing import List


class Melt:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:

        ans = [0] * n
        _len = len(bookings)

        for i in range(1, n + 1):
            for j in range(_len):
                start, end, seats = bookings[j][0], bookings[j][1], bookings[j][2]

                if start <= i <= end:
                    ans[i - 1] += seats

        return ans



m = Melt()
print(m.corpFlightBookings([[1, 2, 10], [2, 3, 20], [2, 5, 25]], 5))

# def test_corp():
#     m = Melt()
#     assert m.corpFlightBookings([[1, 2, 10], [2, 3, 20], [2, 5, 25]], 5) == [10, 55, 45, 25, 25]
#     assert m.corpFlightBookings([[1, 2, 10], [2, 2, 15]], 2) == [10, 25]
