# Desktop Organizer

A simple Python-based desktop organizer with a minimalistic interface. This program moves all files and selected folders from your desktop into a new folder named "Organized," excluding the files and folders you choose as exceptions.

## Features

- Customize which files and folders to exclude from the organization process
- Dark-themed interface
- Supports moving both files and folders (optional)

## Installation

1. Ensure you have Python 3.x installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).

2. Clone this repository or download the source code as a ZIP file.

\```sh
git clone https://github.com/yourusername/desktop-organizer.git
\```

3. (Optional) If you want to use a virtual environment, navigate to the project folder and create one using the following command:

\```sh
python -m venv venv
\```

4. Activate the virtual environment (if you created one):

- On Windows:

\```sh
venv\Scripts\activate
\```

5. Install the required dependencies (if any) using pip:

\```sh
pip install -r requirements.txt
\```

## Usage

1. Run the `main.py` script:

\```sh
python main.py
\```

2. The interface will appear, displaying a list of files and folders on your desktop.

3. Select the files you want to exclude from the organization process.

4. (Optional) Check the "Include folders" checkbox if you want to move folders as well.

5. Click the "Select Exceptions and Move Files" button. The program will move the selected files and folders to the "Organized" folder on your desktop.

6. A success message will appear once the process is complete.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
