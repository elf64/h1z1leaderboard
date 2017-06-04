# Python 2.7
# Library: requests
import h1z1Leader
import sys

getInfo = h1z1Leader.GetRank(sys.argv[1], sys.argv[2])
getInfo.get_all()
