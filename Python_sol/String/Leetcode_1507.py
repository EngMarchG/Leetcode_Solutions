class Solution:
    def reformatDate(self, date: str) -> str:
        date = date.split()
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        hmap = {month: f"0{x+1}" if x < 9 else f"{x+1}" for x, month in enumerate(months)}

        date[0] = date[0][:-2]
        date[0] = "0" + date[0] if int(date[0])<10 else date[0]
        return f"{date[-1]}-{hmap[date[1]]}-{date[0]}"