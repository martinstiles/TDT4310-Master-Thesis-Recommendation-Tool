class Parser():

    def __init__(self, file):
        self.file = file
        self.rows = []
        # Used for adding weekdays to each row
        self.weekdays = ["monday", "tuesday", "wednesday",
                         "thursday", "friday", "saturday", "sunday"]

    def parse_file(self):
        """
        Parses CSV-file of viewings and adds formatted values to the list rows.
        """
        with open(self.file) as file:
            file_string = file.read()
            lines = file_string.split("\n")
            # Remove column headers and EOF line
            lines.pop(0)
            lines.pop()

            # Unique day counter
            day = 0
            # The first date in the dataset
            old_date = "20180101"

            for i in range(len(lines)):
                # Each line is added as a new list in rows
                self.rows.append(lines[i].split(","))

                # This makes sure the day is only incremented on new days
                new_date = self.rows[i][1]
                if new_date != old_date:
                    day += 1
                old_date = new_date

                # Some columns are formatted, and the weekday column is added
                self.rows[i][0] = self.format_series(self.rows[i][0])
                self.rows[i][1] = self.format_date(self.rows[i][1])
                self.rows[i].append(self.weekdays[day % 7])

    def format_series(self, series_id):
        return series_id.replace("-", " ")

    def format_date(self, date):
        year = date[:4]
        month = date[4:6]
        day = date[6:]
        return year + "-" + month + "-" + day
