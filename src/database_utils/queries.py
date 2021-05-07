from connector import *
from tabulate import tabulate


class Cursor():

    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()

    def select_all_viewings(self, limit=-1):
        """
        Query all rows in the viewings table, with option to limit number of rows.
        :param limit: an optional number specifying row limit
        :return: Cursor object containing result 
        """
        self.cursor.execute("SELECT * FROM Viewings LIMIT ?", (limit,))

        print_table(self.cursor)
        return self.cursor

    # def select_most_popular_series(self, limit=-1):
    #     """
    #     Query the viewings with the most views, grouped by series, with option to limit number of rows.
    #     :param limit: an optional number specifying row limit
    #     :return: Cursor object containing result
    #     """
    #     query = """ SELECT series_id, SUM(views) AS total_views FROM Viewings
    #                 GROUP BY series_id
    #                 ORDER BY total_views DESC
    #                 LIMIT ?
    #             """
    #     self.cursor.execute(query, (limit,))

    #     print_table(self.cursor)
    #     return self.cursor

    # def select_average_viewings_by_weekday(self, series_id):
    #     """
    #     Query average number of viewings of a given series per day
    #     :param series_id: name of the series requested
    #     :return: Cursor object containing result
    #     """
    #     query = """ SELECT series_id, weekday, ROUND(AVG(views), 0) AS average_views FROM Viewings
    #                 WHERE series_id=?
    #                 GROUP BY weekday
    #                 ORDER BY average_views DESC
    #             """
    #     self.cursor.execute(query, (series_id,))

    #     print_table(self.cursor)
    #     return self.cursor

    # def select_average_viewings_by_screen(self, series_id):
    #     """
    #     Query average number of viewings of a given series per screen.
    #     :param series_id: name of the series requested
    #     :return: Cursor object containing result
    #     """
    #     query = """ SELECT series_id, screen, ROUND(AVG(views), 0) AS average_views FROM Viewings
    #                 WHERE series_id=?
    #                 GROUP BY screen
    #                 ORDER BY average_views DESC
    #             """
    #     self.cursor.execute(query, (series_id,))

    #     print_table(self.cursor)
    #     return self.cursor

    # def select_series_viewings(self, series_id, screen, start_date, end_date):
    #     """
    #     Query number of viewings of a given series on a given screen type in a given time frame
    #     :param series_id: name of the series requested
    #     :return: Cursor object containing result
    #     """
    #     query = """ SELECT series_id, date, screen, views FROM Viewings
    #                     WHERE series_id=:series_id AND screen=:screen AND date>=:start_date AND date<:end_date
    #                 """
    #     self.cursor.execute(
    #         query, {"series_id": series_id, "screen": screen, "start_date": start_date, "end_date": end_date})

    #     print_table(self.cursor)
    #     return self.cursor
