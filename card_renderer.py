# card_renderer.py
from jinja2 import Environment, FileSystemLoader

# A dictionary holding all the color themes we can use.
THEMES = {
    "default": {
        "background": "#1E1E1E", "border": "#7A7A7A", "prompt": "#00FF41",
        "command": "#FFFFFF", "output_label": "#C5C5C5", "output_value": "#FFFFFF",
    },
    "amber": {
        "background": "#211B00", "border": "#B8860B", "prompt": "#FFB000",
        "command": "#F0E68C", "output_label": "#D2B48C", "output_value": "#FFD700",
    },
    "ocean": {
        "background": "#001F3F", "border": "#0074D9", "prompt": "#7FDBFF",
        "command": "#FFFFFF", "output_label": "#AAAAAA", "output_value": "#F0F8FF",
    },
        "arch": {
        "background": "#0C0C0C", # A very dark, almost black background
        "border": "#5A5A5A",     # A subtle grey border
        "prompt": "#1793D1",     # The iconic Arch blue for the prompt
        "command": "#EFEFEF",    # A soft, off-white for user input
        "output_label": "#8F8F8F",# Dimmed grey for non-critical labels
        "output_value": "#EFEFEF", # The same soft white for data
    }
}

# Set up Jinja2 to find our SVG file in the 'templates' folder
env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('stats_card.svg')

def parse_stats_data(stats: dict) -> dict:
    """
    Parses the raw API data and pre-formats numbers for clean display.
    """
    # Extract total question counts
    total_questions_data = {item['difficulty']: item['count'] for item in stats['allQuestionsCount']}
    
    # Extract user's solved counts
    solved_data = {item['difficulty']: item['count'] for item in stats['matchedUser']['submitStats']['acSubmissionNum']}

    # Get the raw numbers
    easy_solved = solved_data.get("Easy", 0)
    medium_solved = solved_data.get("Medium", 0)
    hard_solved = solved_data.get("Hard", 0)
    total_solved = solved_data.get("All", 0)

    return {
        "username": stats['matchedUser']['username'],

        # Pass the original, unformatted numbers for calculations
        "easy_solved_num": easy_solved,
        "medium_solved_num": medium_solved,
        "hard_solved_num": hard_solved,
        "total_easy": total_questions_data.get("Easy", 0),
        "total_medium": total_questions_data.get("Medium", 0),
        "total_hard": total_questions_data.get("Hard", 0),
        "total_questions": total_questions_data.get("All", 0),

        # Pass the pre-formatted strings for display
        "easy_solved_str": f"{easy_solved:<4}",
        "medium_solved_str": f"{medium_solved:<4}",
        "hard_solved_str": f"{hard_solved:<4}",
        "total_solved_str": f"{total_solved:<4}",
    }

def render_svg_card(stats: dict, theme: dict) -> str:
    """Takes the stats and a theme, then renders the SVG card."""
    parsed_data = parse_stats_data(stats)
    return template.render(theme=theme, **parsed_data)