# TimeCalc Pro: Music Programming Utility

**TimeCalc Pro** is a precision duration calculator designed for music producers, sequence programmers, and studio engineers. It simplifies the process of calculating track lengths, set times, and cue timings by using a specialized "Minute.Second" arithmetic.



## 🎹 The Core Rule
Unlike standard calculators, TimeCalc Pro treats decimals as a separator for seconds (Base 60):
* **Before the Decimal:** Minutes.
* **After the Decimal:** Seconds.
* **The Logic:** Adding `0.20` to `1.50` results in `2.10` (2 minutes, 10 seconds), whereas a standard calculator would incorrectly give `1.70`.



---

## 🚀 Workflow Features
* **Express Entry:** Type a duration and immediately follow it with `+` or `-` (e.g., `3.24+`) to update the total instantly. This triggers the calculation the moment the operator is typed, saving a keystroke.
* **Enter-to-Add:** The `Return/Enter` key (and Numpad Enter) is mapped to the **Add** operation for rapid data entry.
* **Session Log:** A real-time, scrollable history showing every operation and the resulting running total.
* **Instant Undo:** Press `Command + Z` (macOS) or `Control + Z` (Windows/Linux) to revert the last action. This removes the last log entry and restores the previous total.
* **System Native UI:** Built with `customtkinter`, the interface automatically follows your macOS **Dark/Light Mode** settings.

---

## 🛠 Installation & Setup
This project is optimized for **uv**, the high-performance Python package and environment manager. Requires Python >=3.11.

### 1. Initialize Environment
If you are setting this up for the first time, run the following in your terminal:
```uv sync```

### 2. Running the App
To launch the calculator locally:
```python TimeCalc.py```

Or with uv:
```uv run python TimeCalc.py```

### 3. Running Tests
To run the test suite:
```uv run pytest```


## 📦 Packaging for macOS (.app)

To bundle the script into a standalone, double-clickable application for macOS:

### Install the builder:
PyInstaller is included in the dev dependencies, so after `uv sync`, it's ready. If needed separately:
```uv add --dev pyinstaller```

### Run the build script:
```pyinstaller TimeCalc.spec```

####Find the App:

Your standalone TimeCalc.app will be located in the dist/ folder. You can now move this to your /Applications folder.

## 🔄 Maintenance & Updates

* **Syncing Dependencies:** If the `pyproject.toml` is updated with new libraries, run `uv sync` to refresh your local environment.
* **Automated Builds:** This repository is configured with a GitHub Action. Simply `git push` your changes to the `main` branch, and a new macOS build will be generated automatically as a downloadable "Artifact" in the GitHub Actions tab.
* **Cleaning Builds:** If you encounter issues during packaging, delete the `build/` and `dist/` folders before re-running the `pyinstaller` command to ensure a "clean" compile.

## ⚠️ Usage Notes

* **Auto-Focus:** The application automatically focuses on the input field upon launch and after every calculation, allowing for continuous hands-on-keyboard typing.
* **Security:** Because the generated `.app` is unsigned, macOS Gatekeeper may block it. To bypass this, **Right-Click > Open** the application the first time you run it.
* **Reset:** The **Reset** button clears both the running total and the session log. Note that this action is permanent and cannot be undone via `Cmd+Z`.

## 👏🏼 Comment & Acknowledgement
* This app was quite a climb up the learning curve. It is a first attempt at a full GitHub managed project developed using Gemini, VSCode and GitHub Copilot extension. I am grateful to the developers of these tools. They have removed many of the major barriers to developing and testing ideas in Python.

## 📄 License
This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details.