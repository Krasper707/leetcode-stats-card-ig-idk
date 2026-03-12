from fastapi import FastAPI, HTTPException, Response, Query
from typing import Optional

# Keep your existing imports
from leetcode_fetcher import fetch_leetcode_stats
from card_renderer import render_svg_card, THEMES

app = FastAPI(
    title="LeetCode Stats API",
    description="An API to fetch LeetCode user profile stats."
)

@app.get("/api/stats/{username}")
async def get_user_stats_card(
    username: str, 
    theme: str = Query(default="default") # Use Query for better documentation
):
    """
    An endpoint to get a LeetCode stats SVG card for a specific user.
    """
    
    stats = fetch_leetcode_stats(username)
    
    # Improved Error Handling
    if not stats:
         raise HTTPException(status_code=503, detail="LeetCode API is currently unreachable.")
    
    if not stats.get('matchedUser'):
        raise HTTPException(status_code=404, detail=f"User '{username}' not found.")

    # THEME SELECTION
    if theme not in THEMES:
        theme = "default"
    selected_theme_config = THEMES[theme]

    user_data = stats['matchedUser']
    submit_stats = user_data['submitStatsGlobal']['acSubmissionNum']
    
    processed_stats = {
        "username": username,
        "rank": user_data['profile']['ranking'],
        "total_questions": stats['allQuestionsCount'][0]['count'],
        "total_easy": stats['allQuestionsCount'][1]['count'],
        "total_medium": stats['allQuestionsCount'][2]['count'],
        "total_hard": stats['allQuestionsCount'][3]['count'],
        "total_solved_num": submit_stats[0]['count'],
        "easy_solved_num": submit_stats[1]['count'],
        "medium_solved_num": submit_stats[2]['count'],
        "hard_solved_num": submit_stats[3]['count'],
    }

    # RENDER SVG
    svg_card = render_svg_card(processed_stats, selected_theme_config)

    # OPTIMIZED HEADERS FOR GITHUB
    headers = {
        "Content-Type": "image/svg+xml",
        "Cache-Control": "public, max-age=7200, s-maxage=14400, stale-while-revalidate=3600",
        "Pragma": "no-cache",
        "Expires": "0",
    }
    
    print(f"Successfully generated card for: {username} [Theme: {theme}]")
    
    return Response(content=svg_card, media_type="image/svg+xml", headers=headers)