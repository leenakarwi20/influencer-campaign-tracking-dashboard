import csv
from collections import Counter

FILE_NAME = "campaigns.csv"


def load_campaigns():
    campaigns = []

    with open(FILE_NAME, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            campaigns.append(row)

    return campaigns


def analyse_campaigns(campaigns):
    total_campaigns = len(campaigns)

    status_counts = Counter(
        campaign["status"] for campaign in campaigns
    )

    platform_counts = Counter(
        campaign["platform"] for campaign in campaigns
    )

    completed_campaigns = [
        campaign
        for campaign in campaigns
        if campaign["status"] == "Completed"
    ]

    total_views = sum(
        int(campaign["views"])
        for campaign in completed_campaigns
    )

    total_likes = sum(
        int(campaign["likes"])
        for campaign in completed_campaigns
    )

    total_comments = sum(
        int(campaign["comments"])
        for campaign in completed_campaigns
    )

    return {
        "total_campaigns": total_campaigns,
        "status_counts": status_counts,
        "platform_counts": platform_counts,
        "total_views": total_views,
        "total_likes": total_likes,
        "total_comments": total_comments,
    }


def display_dashboard(results):
    print("=" * 45)
    print("INFLUENCER CAMPAIGN TRACKING DASHBOARD")
    print("=" * 45)

    print(f"\nTotal campaigns: {results['total_campaigns']}")

    print("\nCampaign status:")
    for status, count in results["status_counts"].items():
        print(f"- {status}: {count}")

    print("\nPlatforms:")
    for platform, count in results["platform_counts"].items():
        print(f"- {platform}: {count}")

    print("\nPerformance of completed campaigns:")
    print(f"- Total views: {results['total_views']:,}")
    print(f"- Total likes: {results['total_likes']:,}")
    print(f"- Total comments: {results['total_comments']:,}")

    print("\nAll data used in this demonstration is fictional.")
    print("=" * 45)


campaigns = load_campaigns()
results = analyse_campaigns(campaigns)
display_dashboard(results)
