import stravalib as sl
from decouple import config

client = sl.client.Client(access_token=config('ACCESS_TOKEN'))

segments = []
bounds = [33.7655709,-84.3180585,33.80906,-84.266101]
segments.append(client.explore_segments(bounds, activity_type="running"))
