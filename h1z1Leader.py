import requests

__author__ = "PukaPy"


class GetRank:

    def __init__(self, nameX, region):
        self.nameX = nameX
        self.region = region
        self.carrot = []

        self.regions = {
            "North America": "1",
            "Europe": "2",
            "South America": "3",
            "Asia/Pacific": "4",
            "Australia": "5"
        }

        self.ranks = {
            "Bronze": "1",
            "Silver": "2",
            "Gold": "3",
            "Platinum": "4",
            "Diamond": "5",
            "Royalty": "6"
        }

        self.headers = {
            "Host": "census.daybreakgames.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0)"
                          " Gecko/20100101 Firefox/53.0",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Referer": "https://www.h1z1.com/king-of-the-kill/leaderboards?" \
                       "region={}&pageLength=25&page=1&searchText={}".format(self.region, self.nameX),
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        }

        self.params = {
            "pageSize": "25",
            "filterKey": "s4_r{}_g1".format(self.region),
            "pageNumber": "1",
            "name": "{}".format(nameX)
        }

        self.url = 'https://census.daybreakgames.com/rest/leaderboard/kotk/name-search-get-page'

    def getRegions(self):
        """
        Get the id for every region
        :return:
        """
        for k, v in self.regions.items():
            print "Region: {} With ID -> {}".format(k, v)

    def PrintShiny(self, Scores):
        if len(Scores["score"]) < 6:
            self.carrot.append("Score:   {:,} > ".format(
                int(Scores["score"])
            ))
        else:
            self.carrot.append("Score:  {:,} > ".format(
                int(Scores["score"])
            ))
        if len(Scores["kills"]) >= 2:
            self.carrot.append("Kills: [ {:,}] >  ".format(
                int(Scores["kills"])
            ))
        else:
            self.carrot.append("Kills: [ {:,} ] >  ".format(
                int(Scores["kills"])
            ))
        if len(Scores["rank"]) >= 2:
            self.carrot.append("Place: [ {:,}]".format(
                int(Scores["rank"])
            ))
        else:
            self.carrot.append("Place: [ {:,} ]".format(
                int(Scores["rank"])
            ))
        print ''.join(self.carrot)
        del self.carrot[:]

    def get_all(self):
        """
        Get all info about the player
        Ex:
        Top10, Top kills, Total Kills,
          Wins per match ratio, etc..
        :return:
        """

        session = requests.session()
        p = session.post(
            self.url,
            params=self.params,
            headers=self.headers
        )
        last_j = p.json()

        # Assign the current Rank ex(1,2,3..6) to rank variable
        # and the sub-rank to the sub_rank variable
        try:
            rank = last_j["successPayload"]["rows"][0]["values"]["tier"]
            sub_rank = last_j["successPayload"]["rows"][0]["values"]["subtier"]
        except IndexError:
            print "User not found!"
            quit()

        #
        # Get player rank
        #
        for k, v in self.ranks.items():
            if rank == v:
                rank = k
        #
        # Print name, position
        #
        print "\n\nUser : {}\n".format(
            last_j["successPayload"]["rows"][0]["values"]["user_name"]
        ), "\nIn position {:,}\n-----------------\nTop 10 Matches!\n-----------------".format(
            int(last_j["successPayload"]["rows"][0]["position"])
        )
        #
        # Print top10 matches
        #
        for i in range(0, 10):
            scores = last_j["successPayload"]["rows"][0]["detail"]["top_matches"][i]
            self.PrintShiny(scores)

        print "-----------------\r\n"
        #
        # Print Leader board info
        #
        print "Kills per Match Ratio: {}\n" \
              "Wins per Match Ratio: {}\n" \
              "Top10 Per Match Ratio: {}\n" \
              "Top10 Total Score: {:,}\n" \
              "Top Kills: {:,}\n" \
              "Total Matches: {:,}\n" \
              "Total Wins: {:,}\n" \
              "Total Kills: {:,}\n" \
              "\n--> RANK: {} {} <--\n"\
            .format(
                float(last_j["successPayload"]["rows"][0]["values"]["kills_per_match"]),
                float(last_j["successPayload"]["rows"][0]["values"]["wins_per_match"]),
                float(last_j["successPayload"]["rows"][0]["values"]["top_tens_per_match"]),
                int(last_j["successPayload"]["rows"][0]["values"]["top_10_total_score"]),
                int(last_j["successPayload"]["rows"][0]["values"]["top_kills"]),
                int(last_j["successPayload"]["rows"][0]["values"]["total_matches"]),
                int(last_j["successPayload"]["rows"][0]["values"]["total_wins"]),
                int(last_j["successPayload"]["rows"][0]["values"]["total_kills"]),
                rank, sub_rank
            )

