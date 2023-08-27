# import requests

# cookies = {
#     'guest_id': 'v1%3A169314187738854698',
#     'guest_id_marketing': 'v1%3A169314187738854698',
#     'guest_id_ads': 'v1%3A169314187738854698',
#     'gt': '1695786161162391552',
#     'att': '1-Oi73szx4Pi10rtA9c8EzjfxhDG1fXWvQct2iw81X',
#     '_twitter_sess': 'BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCPslHzeKAToMY3NyZl9p%250AZCIlNzk4OTQ4ZmRhYWM1NGQ3ZmEyMDI4MTRiMTE0ZGI1Zjc6B2lkIiVkZjhk%250AZDFiOTI5M2UzMTUzNWYzM2RmOTJlZDhlOWNkMw%253D%253D--79e5b1291172e59f7998c4b038c92ca9f695de83',
#     'personalization_id': '"v1_czNGJpB+AHOucozq7A2+ng=="',
#     'ct0': '3b95dc7aa639111be12c4b041020607b',
# }

# headers = {
#     'authority': 'twitter.com',
#     'accept': '*/*',
#     'accept-language': 'en-US,en;q=0.8',
#     'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
#     'content-type': 'application/json',
#     # 'cookie': 'guest_id=v1%3A169314187738854698; guest_id_marketing=v1%3A169314187738854698; guest_id_ads=v1%3A169314187738854698; gt=1695786161162391552; att=1-Oi73szx4Pi10rtA9c8EzjfxhDG1fXWvQct2iw81X; _twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCPslHzeKAToMY3NyZl9p%250AZCIlNzk4OTQ4ZmRhYWM1NGQ3ZmEyMDI4MTRiMTE0ZGI1Zjc6B2lkIiVkZjhk%250AZDFiOTI5M2UzMTUzNWYzM2RmOTJlZDhlOWNkMw%253D%253D--79e5b1291172e59f7998c4b038c92ca9f695de83; personalization_id="v1_czNGJpB+AHOucozq7A2+ng=="; ct0=3b95dc7aa639111be12c4b041020607b',
#     'referer': 'https://twitter.com/FiersaBesari/status/1313990655698329600',
#     'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Brave";v="116"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"macOS"',
#     'sec-fetch-dest': 'empty',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-site': 'same-origin',
#     'sec-gpc': '1',
#     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
#     'x-client-transaction-id': 'yQwiz4mxmqLqoA5BXPZfZOpnCXSpMOMnWnPAEa+Sq/ZyMje9hcaExn6xIpzTXQLNHO84Uskmitg/U2WjyYeS4z++aSCqyA',
#     'x-csrf-token': '3b95dc7aa639111be12c4b041020607b',
#     'x-guest-token': '1695786161162391552',
#     'x-twitter-active-user': 'yes',
#     'x-twitter-client-language': 'en',
# }

# params = {
#     'variables': '{"tweetId":"1313990655698329600","withCommunity":false,"includePromotedContent":false,"withVoice":false}',
#     'features': '{"creator_subscriptions_tweet_preview_api_enabled":true,"tweetypie_unmention_optimization_enabled":true,"responsive_web_edit_tweet_api_enabled":true,"graphql_is_translatable_rweb_tweet_is_translatable_enabled":true,"view_counts_everywhere_api_enabled":true,"longform_notetweets_consumption_enabled":true,"responsive_web_twitter_article_tweet_consumption_enabled":false,"tweet_awards_web_tipping_enabled":false,"freedom_of_speech_not_reach_fetch_enabled":true,"standardized_nudges_misinfo":true,"tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled":true,"longform_notetweets_rich_text_read_enabled":true,"longform_notetweets_inline_media_enabled":true,"responsive_web_graphql_exclude_directive_enabled":true,"verified_phone_label_enabled":false,"responsive_web_media_download_video_enabled":false,"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,"responsive_web_graphql_timeline_navigation_enabled":true,"responsive_web_enhance_cards_enabled":false}',
# }

# response = requests.get(
#     'https://twitter.com/i/api/graphql/0hWvDhmW8YQ-S_ib3azIrw/TweetResultByRestId',
#     params=params,
#     cookies=cookies,
#     headers=headers,
# )

# print(response.json())

import httpx

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
}


# retrieve embed HTML
with httpx.Client(http2=True, headers=HEADERS) as client:
    response = client.get(
        "https://cdn.syndication.twimg.com/tweet-result?id=1664267318053179398&lang=en",
    )
    assert response.status_code == 200
    data = response.json()
    print(data)
