import requests
from .exceptions import *


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

        ret = self.session.get(self.host + url, params=params).json()
        if ret["success"] == 0:
            return ret["error"]
        else:
            return ret["data"]

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
            if 'upcoming' or 'inplay' or 'ended' in type:
                params['type'] = type

            else:
                raise InvalidOption

        if columns is not None:
            params['columns'] = columns

        if page is not None:
            params['page'] = page

        res = self._get('match/today', params=params)
        if isinstance(res, dict):
            return res
        else:
            return TotalCornerAPI.formatter(res)


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

        res = self._get('match/schedule', params=params)
        if isinstance(res, dict):
            return res
        else:
            return TotalCornerAPI.formatter(res)

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

        res = self._get('match/view/' + str(matchid), params=params)
        if isinstance(res, dict):
            return res
        else:
            return TotalCornerAPI.formatter(res)

    def odds(self, matchid, columns="asianList,goalList,cornerList,oddsList,asianHalfList,goalHalfList,"
                                    "cornerHalfList,oddsHalfList"):
        """

        :param matchid:
        :param columns:
        :return:
        """

        params = {'token': self.apikey}

        if columns is not None:
            params['columns'] = columns

        res = self._get('match/odds/' + str(matchid), params=params)
        if isinstance(res, dict):
            return res
        else:
            return TotalCornerAPI.formatter(res)

    def leaguetable(self, leagueid, type='table'):
        """

        :param leagueid:
        :param type:
        :return:
        """
        if "table" or "cards" or "corner" in type:
            params = {'token': self.apikey, 'type': type}
        else:
            raise InvalidOption

        res = self._get('league/table/' + str(leagueid), params=params)
        return res

    def leagueschedule(self, leagueid, page=None,
                       columns='events,odds,asian,cornerLine,cornerLineHalf,goalLine,goalLineHalf,"asianCorner,attacks,dangerousAttacks,shotOn,shotOff,possession'):
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

        res = self._get('league/schedule/' + str(leagueid), params=params)
        if isinstance(res, dict):
            return res
        else:
            match = res.pop("matches")
            m = TotalCornerAPI.formatter(match)
            res["matches"] = m
            return res

    @staticmethod
    def formatter(data: list):
        for item in data:
            item["home"] = item.pop("h")
            item["home_id"] = item.pop("h_id")
            item["away"] = item.pop("a")
            item["away_id"] = item.pop("a_id")
            item["league"] = item.pop("l")
            item["league_id"] = item.pop("l_id")
            item["home_corners"] = item.pop("hc")
            item["away_corners"] = item.pop("ac")
            item["home_goals"] = item.pop("hg")
            item["away_goals"] = item.pop("ag")
            item["home_red_cards"] = item.pop("hrc")
            item["away_red_cards"] = item.pop("arc")
            item["home_yellow_cards"] = item.pop("hyc")
            item["away_yellow_cards"] = item.pop("ayc")
            item["half_home_corner"] = item.pop("hf_hc")
            item["half_away_corner"] = item.pop("hf_ac")
            item["half_home_goals"] = item.pop("hf_hg")
            item["half_away_goals"] = item.pop("hf_ag")
            if "ish" in item.keys():
                if item["ish"] == "0":
                    item.pop("ish")
                    item["half"] = "first"
                elif item["ish"] == "1":
                    item.pop("ish")
                    item["half"] = "second"
            if "hp" in item.keys():
                item["home_league_pos"] = item.pop("hp")
            if "ap" in item.keys():
                item["away_league_pos"] = item.pop("ap")
            if "events" in item.keys():
                if item["events"] is not None:
                    for e in item["events"]:
                        if "tp" in e.keys():
                            if e["tp"] == "c":
                                e["type"] = "corner"
                            elif e["tp"] == "g":
                                e["type"] = "goal"
                            elif e["tp"] == "rc":
                                e["type"] = "red_card"
                            e.pop("tp")
                        if "h" in e.keys():
                            if e["h"] == "h":
                                e["side"] = "home"
                            elif e["h"] == "a":
                                e["side"] = "away"
                            e.pop("h")
                        if "t" in e.keys():
                            e["time"] = e.pop("t")
            if "p_odds" in item.keys():
                item["pre_match_odds"] = item.pop("p_odds")
            if "po_odds" in item.keys():
                item["pre_match_opening_odds"] = item.pop("po_odds")
            if "i_odds" in item.keys():
                item["inplay_odds"] = item.pop("i_odds")
            if "p_asian" in item.keys():
                item["asian_handicap"] = item.pop("p_asian")
            if "i_asian" in item.keys():
                item["asian_handicap_inplay"] = item.pop("i_asian")
            if "p_corner" in item.keys():
                item["corner_line"] = item.pop("p_corner")
            if "i_corner" in item.keys():
                item["corner_line_inplay"] = item.pop("i_corner")
            if "p_goal" in item.keys():
                item["goal_line"] = item.pop("p_goal")
            if "i_goal" in item.keys():
                item["goal_line_inplay"] = item.pop("i_goal")
            if "asian_corner" in item.keys():
                item["asian_handicap_cornenr"] = item.pop("asian_corner")
            if "attacks_h" in item.keys():
                item["halftime_attacks"] = item.pop("attacks_h")
            if "p_corner_h" in item.keys():
                item["corner_line_half"] = item.pop("p_corner_h")
            if "i_corner_h" in item.keys():
                item["corner_line_inplay_half"] = item.pop("i_corner_h")
            if "i_goal_h" in item.keys():
                item["goal_line_inplay_half"] = item.pop("i_goal_h")
            if "p_goal_h" in item.keys():
                item["goal_line_half"] = item.pop("p_goal_h")

        return data



