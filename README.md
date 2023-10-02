# IDS_Lite

## Intrusion Detection System (IDS)

An open-source Intrusion Detection System crafted with Python and Scapy, complemented by a user-friendly GUI via PyQt.

# WORK IN PROGRESS

Using this project as a way to go deeper into security engineering, GUI development, and Scapy. This will continue to develop over time. It is a personal passion project, but as with all open-source code, all contributions and support/feedback are welcomed and encouraged.

---

## 🚀 Features

- 🔍 **Real-time Packet Capture and Analysis**: Dive deep into network traffic as it happens.
- 🛡 **Signature and Anomaly-based Detection**: Catch malicious activities from known patterns and unusual behaviors.
- 🖥 **Interactive GUI**: Seamlessly configure, monitor, and respond using a modern interface.
- 📝 **Comprehensive Logging & Alerts**: Stay informed with detailed logs and instant alerts.
- ⚙️ **Modular Design**: Extend and integrate as per unique needs.

---

## 📋 Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## 🛠 Installation

1. **Get the Source**: Clone the GitHub repository.
    ```bash
    git clone https://github.com/YourUsername/Intrusion-Detection-System.git
    cd Intrusion-Detection-System
    ```

2. **Virtual Environment (Recommended)**: Isolate your project dependencies.
    ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows? Use `env\Scripts\activate`
    ```

3. **Dependency Installation**: Install the necessary Python packages.
    ```bash
    pip install -r requirements.txt
    ```

---

## 🚀 Usage

### 🌐 Starting the IDS

1. **Activate the Environment**: Before running the IDS, always activate the virtual environment.
    ```bash
    source env/bin/activate  # On Windows? Use `env\Scripts\activate`
    ```

2. **Run the IDS**:
    ```bash
    python src/main.py
    ```

3. **GUI Interface**: The GUI should now launch. Use it to:
   - Configure the IDS settings.
   - Monitor live network traffic.
   - Review alerts and logs.
   - Manage signature databases (if applicable).

### 🛠 Configuration & Customization

- All configurations are accessible via the GUI. However, for advanced users, direct configuration modifications can be made in `src/utils/config.py`.

- Custom alerting and packet analysis modules can be integrated by modifying `src/analyzer.py` and `src/utils/alerts.py` respectively.

---

## 🧪 Testing

### 🔄 Running Tests

1. **Activate the Environment**: Ensure you're working within the project's virtual environment.
    ```bash
    source env/bin/activate  # On Windows? Use `env\Scripts\activate`
    ```

2. **Run Tests**: Use `pytest` to execute the suite of tests.
    ```bash
    pytest tests/
    ```

### ✅ Test Suite Breakdown

- **Packet Capture Tests**: Ensures that the system correctly captures packets in various network conditions. (`tests/test_capture.py`)

- **Analyzer Tests**: Verifies the accuracy and efficiency of packet analysis algorithms. (`tests/test_analyzer.py`)

- **GUI Tests**: Basic sanity checks to ensure GUI components load and function as expected. (`tests/test_gui.py`)

- **Utility Tests**: Validates helper functions, alert mechanisms, and configuration management. (`tests/test_utils.py`)

### 🔁 Continuous Integration

- If integrating with platforms like Jenkins, Travis CI, or GitHub Actions, automate the testing process for every push or pull request. It ensures code quality and reduces regressions.

---

## 📚 Documentation

Thorough documentation is available in the `docs/` directory. It covers:

- **Software Architecture**: Understand the design principles and flow of the IDS. (`docs/architecture.md`)

- **GUI Design**: Dive deep into the GUI's design, features, and customization options. (`docs/gui_design.md`)

- **User Guide**: A step-by-step walkthrough for end-users on how to operate and make the most of the IDS. (`docs/usage_guide.md`)

To contribute to documentation, please follow the same guidelines mentioned in [Contributing](#contributing).

## 🤝 Contributing

Open-source projects thrive on contributions. Here's how you can join the action:

1. **Fork the Project**: Click the `Fork` button on the top right of the main repository page.
2. **Clone Your Fork**: Open your terminal and run:
    ```bash
    git clone https://github.com/ConnorBritain/ids-lite.git
    ```
3. **Navigate to the Directory**:
    ```bash
    cd ids-lite
    ```
4. **Create a New Branch**:
    ```bash
    git checkout -b feature/AmazingFeature
    ```
5. **Make Changes & Commit**:
    ```bash
    git add .
    git commit -m 'Describe your changes here'
    ```
6. **Push the Changes**:
    ```bash
    git push origin feature/AmazingFeature
    ```
7. **Open a Pull Request**: Navigate back to your fork on GitHub and click `New Pull Request`.

---

## ⚖️ License

This project is licensed under the MIT License. Details can be found in the [`LICENSE`](LICENSE) file.

---

## 📧 Contact

**Connor England**   
📥 [Send Email](mailto:connor.r.england.com)   
🌍 [GitHub Profile](https://github.com/ConnorBritain)