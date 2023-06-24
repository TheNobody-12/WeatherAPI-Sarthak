# WeatherAPI-Sarthak

description: A simple weather app using the OpenWeatherMap API

GitHub Copilot is used to assist in the development of the weather API code by providing suggestions and auto-completions based on patterns and examples from existing code. Here's how GitHub Copilot is used in the different parts of the code:
1. Importing libraries:
   - When typing `import requests`, GitHub Copilot provided suggestions to import the `requests` library since it recognizes the need for making HTTP requests.
   - Similarly, when typing `import os`, GitHub Copilot suggested importing the `os` library based on its knowledge of working with the operating system.

2. Loading environment variables:
   - When typing `from dotenv import load_dotenv`, GitHub Copilot provided suggestions to import the `load_dotenv` function from the `dotenv` library, which is commonly used to load environment variables from a .env file.
   - When typing `APP_ROOT = os.path.join(os.path.dirname(__file__), '.')`, GitHub Copilot suggest this code snippet to help determine the application's root directory.

3. Fetching weather data from the API:
   - When typing `requests.get(url.format(city_name,API_key)).json()`, GitHub Copilot can suggest using the `get` method from the `requests` library to make the API request and automatically generate the code to fetch the JSON response.
   - GitHub Copilot can also assist in generating code to handle the API response and extract the required weather data using key access.

4. Error handling:
   - When typing the `try-except` block, GitHub Copilot gave suggestions to handle potential errors that may occur during the execution of the code. It can generate the code to catch and handle exceptions appropriately.

5. Command-line interaction:
   - When prompting the user to enter the city name with `input("Enter the city name: ")`, GitHub Copilot suggest using the `input` function to receive user input.

6. Printing output:
   - GitHub Copilot provide suggestions for printing the weather data to the command line using formatted strings.

Throughout the development process, GitHub Copilot assisted by completing code snippets, generating function signatures, suggesting variable names, and providing relevant code examples based on the context and the task at hand. It help to save time and increase productivity by automating repetitive or boilerplate code segments. However, it's important to review and verify the suggestions provided by Copilot to ensure the code meets the desired requirements and quality standards.

## Installation

1. Clone the repo
   ```sh
   git clone https://github.com/TheNobody-12/WeatherAPI-Sarthak.git
    ```
2. Install python packages
   ```sh
   pip install -r requirements.txt
   ```
3. Run the app
   ```sh
    python data.py
    ```

## Usage

1. Enter the city name

#### Output
![image](https://github.com/TheNobody-12/WeatherAPI-Sarthak/assets/75840118/05db8b32-d12f-4d37-811c-67c7a3d69565)

## ❤️ Project Contributor

<table>
	<tr>
		<td align="center">
			<a href="https://github.com/TheNobody-12">
				<img src="https://user-images.githubusercontent.com/75840118/210078270-64c36621-56e4-4cd8-beb6-bcfcb949fe3d.jpg" width="100px" alt="" /> 
				<br /> <sub><b>Sarthak Kapaliya(TheNobody-12)</b></sub>
			</a>
			<br /> <a href="https://github.com/TheNobody-12"> 
		Contributor
	    </a>
		</td>
	</tr>
</table>
