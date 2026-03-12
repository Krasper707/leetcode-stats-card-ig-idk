# 💻 LeetCode Stats Card Generator

A dynamic, customizable, and terminal-themed stats card for your LeetCode profile, ready to be pinned on your GitHub README.

This project is a Python-based web service built with FastAPI and deployed on Vercel. It fetches your latest LeetCode stats and renders them as a beautiful, retro SVG image.

## ✨ Showcase

Here's how it looks with the `arch` theme:

<!--
  IMPORTANT: Replace the URL below with your own live Vercel URL!
  And replace 'Krasper707' with your own LeetCode username.
-->
<p align="center">
  <img 
    src="https://leetcode-stats-card-ig-idk.vercel.app/api/stats/Krasper707?theme=arch" 
    alt="Saurabh's LeetCode Stats"
    style="background-color: #0C0C0C; border-radius: 6px;"
  />
</p>

```
![LeetCode Stats](https://leetcode-stats-card-ig-idk.vercel.app/api/stats/YOUR_USERNAME?theme=arch)
```

## 🔥 Features

- **Dynamically Generated:** Your stats are always up-to-date.
- **Highly Customizable:** Comes with multiple built-in themes to match your style.
- **Authentic Terminal Aesthetic:** Features the `VT323` pixel font, a terminal window frame, and text-based progress bars.
- **Easy to Use:** Just copy a single line of Markdown or HTML to embed it anywhere.
- **Fast & Reliable:** Deployed on Vercel's global edge network with server-side caching for quick load times.
- **Open Source:** Feel free to fork, modify, and deploy your own version!

---

## 🚀 How to Use

Using the card on your GitHub profile is simple. Just replace `YOUR_LEETCODE_USERNAME` with your own LeetCode username in the snippets below.

### Recommended Method (HTML)

This method is recommended because it prevents the "white flash" on page load by setting a background color for the image container.

<p align="center">
  <img
    src="https://leetcode-stats-card-ig-idk.vercel.app/api/stats/Krasper707?theme=arch&v=2"
    alt="My LeetCode Stats"
    style="background-color: #0C0C0C; border-radius: 6px;"
  />
</p>

### Simple Method (Markdown)

This is simpler but may cause a white box to flash before the image loads on dark-themed READMEs.

![My LeetCode Stats](https://leetcode-stats-card-ig-idk.vercel.app/api/stats/Krasper707?theme=arch)

### 🎨 Customization & Themes

You can customize the card by adding query parameters to the URL.

| Parameter  | Description                            | Example                           |
| :--------- | :------------------------------------- | :-------------------------------- |
| `username` | **(Required)** Your LeetCode username. | `.../stats/Krasper707`            |
| `theme`    | The color theme for the card.          | `.../stats/Krasper707?theme=arch` |

To update your README, copy the Markdown below. I have organized them into categories (Classic, Modern, and Retro) to make it easier for users to browse.

---

### 🎨 Available Themes

| Theme Name      | Preview                                                                                                                                                                       |
| :-------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Default**     | `?theme=default` <br/> <img src="https://leetcode-stats-card-ig-idk.vercel.app/api/stats/Krasper707?theme=default&v=2" width="400" alt="Default Theme"/>                      |
| **Arch**        | `?theme=arch` <br/> <img src="https://leetcode-stats-card-ig-idk.vercel.app/api/stats/Krasper707?theme=arch&v=2" width="400" alt="Arch Theme"/>                               |
| **Dracula**     | `?theme=dracula` <br/> <img src="https://leetcode-stats-card-ig-idk.vercel.app/api/stats/Krasper707?theme=dracula&v=2" width="400" alt="Dracula Theme"/>                      |
| **Nord**        | `?theme=nord` <br/> <img src="https://leetcode-stats-card-ig-idk.vercel.app/api/stats/Krasper707?theme=nord&v=2" width="400" alt="Nord Theme"/>                               |
| **Cyberpunk**   | `?theme=cyberpunk` <br/> <img src="https://leetcode-stats-card-ig-idk.vercel.app/api/stats/Krasper707?theme=cyberpunk&v=2" width="400" alt="Cyberpunk Theme"/>                |
| **Synthwave**   | `?theme=synthwave` <br/> <img src="https://leetcode-stats-card-ig-idk.vercel.app/api/stats/Krasper707?theme=synthwave&v=2" width="400" alt="Synthwave Theme"/>                |
| **Gruvbox**     | `?theme=gruvbox` <br/> <img src="https://leetcode-stats-card-ig-idk.vercel.app/api/stats/Krasper707?theme=gruvbox&v=2" width="400" alt="Gruvbox Theme"/>                      |
| **Monokai**     | `?theme=monokai` <br/> <img src="https://leetcode-stats-card-ig-idk.vercel.app/api/stats/Krasper707?theme=monokai&v=2" width="400" alt="Monokai Theme"/>                      |
| **Ocean**       | `?theme=ocean` <br/> <img src="https://leetcode-stats-card-ig-idk.vercel.app/api/stats/Krasper707?theme=ocean&v=2" width="400" alt="Ocean Theme"/>                            |
| **Amber**       | `?theme=amber` <br/> <img src="https://leetcode-stats-card-ig-idk.vercel.app/api/stats/Krasper707?theme=amber&v=2" width="400" alt="Amber Theme"/>                            |
| **Matrix**      | `?theme=matrix` <br/> <img src="https://leetcode-stats-card-ig-idk.vercel.app/api/stats/Krasper707?theme=matrix&v=2" width="400" alt="Matrix Theme"/>                         |
| **Rose Pine**   | `?theme=rose-pine` <br/> <img src="https://leetcode-stats-card-ig-idk.vercel.app/api/stats/Krasper707?theme=rose-pine&v=2" width="400" alt="Rose Pine Theme"/>                |
| **Solarized**   | `?theme=solarized-dark` <br/> <img src="https://leetcode-stats-card-ig-idk.vercel.app/api/stats/Krasper707?theme=solarized-dark&v=2" width="400" alt="Solarized Dark Theme"/> |
| **Retro White** | `?theme=retro-white` <br/> <img src="https://leetcode-stats-card-ig-idk.vercel.app/api/stats/Krasper707?theme=retro-white&v=2" width="400" alt="Retro White Theme"/>          |

## 🛠️ Running Locally

Want to run this project on your own machine? Here’s how:

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/Krasper707/leetcode-stats-card-ig-idk.git
    cd leetcode-stats-card-ig-idk
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    # On Windows
    .\venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the server:**
    ```bash
    uvicorn main:app --reload
    ```
    Your local server will be running at `http://127.0.0.1:8000`.

## 💻 Tech Stack

- **Backend:** Python, FastAPI
- **Templating:** Jinja2
- **Deployment:** Vercel

## 📄 License

This project is distributed under the MIT License. See the `LICENSE` file for more information.
