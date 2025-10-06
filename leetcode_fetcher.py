import requests
import json

LEETCODE_API_URL = "https://leetcode.com/graphql"

STATS_QUERY = """
query getUserProfile($username: String!) {
    allQuestionsCount {
        difficulty
        count
    }
    matchedUser(username: $username) {
        username
        submitStats: submitStatsGlobal {
            acSubmissionNum {
                difficulty
                count
            }
        }
    }
}
"""

def fetch_leetcode_stats(username: str):
    """
    Sends the query to LeetCode's API to fetch user stats.
    """
    print(f"Fetching stats for user: {username}...")
    
    # Prepare the payload to send
    payload = {
        "query": STATS_QUERY,
        "variables": {
            "username": username
        }
    }
    
    try:
        # Send the request as a POST
        response = requests.post(
            LEETCODE_API_URL, 
            json=payload,
            headers={'User-Agent': 'Mozilla/5.0'} 
        )
        response.raise_for_status() # Raise an error for bad responses (4xx or 5xx)
        
        data = response.json()
        
        if 'errors' in data:
            print(f"LeetCode API returned an error: {data['errors']}")
            return None
            
        print("Successfully fetched stats!")
        return data['data']

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while making the request: {e}")
        return None

if __name__ == "__main__":
    test_username = "Krasper707" 
    stats = fetch_leetcode_stats(test_username)
    
    if stats:
        print(json.dumps(stats, indent=2))