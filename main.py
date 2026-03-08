from fastapi import FastAPI, HTTPException, Response
from typing import Optional

# Keep your existing imports
from leetcode_fetcher import fetch_leetcode_stats
from card_renderer import render_svg_card, THEMES

app = FastAPI(
    title="LeetCode Stats API",
    description="An API to fetch LeetCode user profile stats."
)

@app.get("/api/stats/{username}")
async def get_user_stats_card(username: str, theme: Optional[str] = "default"):
    """
    An endpoint to get a LeetCode stats SVG card for a specific user.
    Supports themes via the ?theme= query parameter (e.g., ?theme=amber).
    """
    
    # --- 1. ANALYTICS LOGGING ---
    # This prints to Vercel logs. You can filter logs later for "STATS_REQUEST_FOR"
    # to count how many unique users are using your tool.
    print(f"STATS_REQUEST_FOR: {username}")
    
    # Fetch stats
    stats = fetch_leetcode_stats(username)
    
    if not stats or not stats.get('matchedUser'):
        raise HTTPException(status_code=404, detail="User not found or LeetCode API error.")
        
    # Theme selection logic
    selected_theme = THEMES.get(theme, THEMES["default"])
    
    # Render SVG
    svg_card = render_svg_card(stats, selected_theme)
    
    # --- 2. VERCEL EDGE CACHING ---
    # We replaced your old 'no-cache' headers.
    # public: Allows Vercel CDN to cache it.
    # max-age=14400: Browser caches it for 4 hours.
    # s-maxage=14400: Vercel CDN caches it for 4 hours.
    
    return Response(
        content=svg_card, 
        media_type="image/svg+xml",
        headers={
            'Cache-Control': 'public, max-age=14400, s-maxage=14400',
        }
    )
