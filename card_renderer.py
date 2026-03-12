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
    },
    # --- NEW THEMES ---
    "dracula": {
        "background": "#282a36", "border": "#44475a", "prompt": "#50fa7b",
        "command": "#f1fa8c", "output_label": "#8be9fd", "output_value": "#bd93f9",
    },
    "nord": {
        "background": "#2e3440", "border": "#4c566a", "prompt": "#88c0d0",
        "command": "#d8dee9", "output_label": "#94a3b8", "output_value": "#eceff4",
    },
    "gruvbox": {
        "background": "#282828", "border": "#7c6f64", "prompt": "#b8bb26",
        "command": "#ebdbb2", "output_label": "#a89984", "output_value": "#fabd2f",
    },
    "cyberpunk": {
        "background": "#000b1e", "border": "#0abdc6", "prompt": "#0abdc6",
        "command": "#ea00d9", "output_label": "#711c91", "output_value": "#fec7d7",
    },
    "synthwave": {
        "background": "#2b213a", "border": "#ff7edb", "prompt": "#36f9f6",
        "command": "#fe4450", "output_label": "#72f1b8", "output_value": "#fede5d",
    },
    "monokai": {
        "background": "#272822", "border": "#49483e", "prompt": "#a6e22e",
        "command": "#f92672", "output_label": "#66d9ef", "output_value": "#fd971f",
    },
    "matrix": {
        "background": "#000000", "border": "#003b00", "prompt": "#00ff41",
        "command": "#008f11", "output_label": "#00ff41", "output_value": "#d1ffda",
    },
    "rose-pine": {
        "background": "#191724", "border": "#403d52", "prompt": "#eb6f92",
        "command": "#f6c177", "output_label": "#908caa", "output_value": "#e0def4",
    },
    "solarized-dark": {
        "background": "#002b36", "border": "#073642", "prompt": "#859900",
        "command": "#268bd2", "output_label": "#93a1a1", "output_value": "#eee8d5",
    },
    "retro-white": { # Classic 90s terminal/System 7 look
        "background": "#ffffff", "border": "#000000", "prompt": "#000000",
        "command": "#0000ff", "output_label": "#666666", "output_value": "#000000",
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