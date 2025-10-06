import time
from fastapi import FastAPI, HTTPException
from typing import Optional

from fastapi.responses import Response

from leetcode_fetcher import fetch_leetcode_stats
from card_renderer import render_svg_card, THEMES
CACHE = {}
CACHE_DURATION_SECONDS = 7200 

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
    
    stats = fetch_leetcode_stats(username)
    
    if not stats or not stats.get('matchedUser'):
        raise HTTPException(status_code=404, detail="User not found or LeetCode API error.")
        
    # Get the dictionary of colors for the requested theme.
    # If the user types a theme that doesn't exist, it safely falls back to the default theme.
    selected_theme = THEMES.get(theme, THEMES["default"])
    
    # Pass the selected theme colors to the renderer.
    svg_card = render_svg_card(stats, selected_theme)
    
    # Return the final SVG image.
    return Response(
        content=svg_card, 
        media_type="image/svg+xml",
        headers={
            'Cache-Control': 'no-cache, no-store, must-revalidate',
            'Pragma': 'no-cache',
            'Expires': '0'
        }
    )