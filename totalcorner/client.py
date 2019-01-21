import requests


class TotalCornerAPI(object):

    def __init__(self, apikey):
        self.apikey = apikey
        self.session = requests.Session()
        self.host = 'https://api.totalcorner.com/v1/'

    def _get(self, url, params):
        """

        :param url:
        :param params:
        :return:
        """

        return self.session.get(self.host + url, params=params).json()

    def today(self, type="upcoming", columns="events,odds,asian,cornerLine,cornerLineHalf,goalLine,goalLineHalf,"
                                       "asianCorner,attacks,dangerousAttacks,shotOn,shotOff,possession", page=None):
        """

        :param type:
        :param columns:
        :param page:
        :return:
        """
        params = {'token': self.apikey}

        if type is not None:
            params['type'] = type

        if columns is not None:
            params['columns'] = columns

        if page is not None:
            params['page'] = page

        return self._get('match/today', params=params)

    def schedule(self, date=None, columns="events,odds,asian,cornerLine,cornerLineHalf,goalLine,goalLineHalf,"
                                       "asianCorner,attacks,dangerousAttacks,shotOn,shotOff,possession", page=None):
        """

        :param date:
        :param columns:
        :param page:
        :return:
        """

        params = {'token': self.apikey}

        if date is not None:
            params['date'] = date

        if columns is not None:
            params['columns'] = columns

        if page is not None:
            params['page'] = page

        return self._get('match/schedule', params=params)

    def matchview(self, matchid, columns="events,odds,asian,cornerLine,cornerLineHalf,goalLine,goalLineHalf,"
                                       "asianCorner,attacks,dangerousAttacks,shotOn,shotOff,possession"):

        """

        :param matchid:
        :param columns:
        :return:
        """

        params = {'token': self.apikey}

        if columns is not None:
            params['columns'] = columns

        return self._get('match/view/' + str(matchid), params=params)

    def odds(self, matchid, columns=None):
        """

        :param matchid:
        :param columns:
        :return:
        """

        params = {'token': self.apikey}

        if columns is not None:
            params['columns'] = columns

        return self._get('match/odds/' + str(matchid), params=params)

    def leaguetable(self, leagueid, type='table'):
        """

        :param leagueid:
        :param type:
        :return:
        """
        params = {'token': self.apikey, 'type': type}

        return self._get('league/table/' + str(leagueid), params=params)

    def leagueschedule(self, leagueid, page=None, columns=None):
        """

        :param leagueid:
        :param page:
        :param columns:
        :return:

        """

        params = {'token': self.apikey}

        if columns is not None:
            params['columns'] = columns

        if page is not None:
            params['page'] = page

        return self._get('league/schedule/' + str(leagueid), params=params)


