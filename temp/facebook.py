from facebook_scraper import get_page_info

info = get_page_info('jkt48.marsha', cookies="cookies.txt")
temp = {
    "name":info.get("Name"),
    "cover_photo":info.get("cover_photo"),
    "profile_picture":info.get("profile_picture"),
    "followers":info.get("followers")
}
print(temp)