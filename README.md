## Twitter Bot

This is a simple Twitter bot that replies to mentions by calling the person who mentioned it as a random animal and returning a humorous insult. For example, the bot might reply to a mention by saying "You are as ugly as a dolphin."

### Installation

1. Clone this repository: `git clone https://github.com/LucasZick/twitterBot.git`
2. Install the required dependencies by running `pip install -r requirements.txt`
3. Create a new Twitter account or use an existing one
4. Apply for a Twitter Developer account and create a new app
5. Generate API keys for the app
6. Set the API keys as environment variables in your system with the following names (fields with double * are required):
    ** `API_KEY`
    ** `API_SECRET_KEY`
    ** `ACCESS_KEY`
    ** `ACCESS_SECRET`
7. Set the application settings in your system with the following names (fields with double * are required):
    ** `REDIS_URL`
    * `PORT`
    * `LOOKUP_TIMEOUT`
    * `LOGLEVEL`
    * `DEBUG`
8. Run the bot with `python3 bot.py`

### Configuration

You can customize the bot's behavior by modifying the `animals.txt` file. This file contains the list of animals the bot can call people. You can add, remove, or modify items in this list to change the bot's behavior.

The `config.py` file sets up the connection and other settings based on the environment variables.

### Contributing

If you want to contribute to this project, feel free to create a pull request with your changes. Make sure to follow the project's code style and add tests for any new functionality.

### License

This project is licensed under the MIT license. See the `LICENSE` file for more information.
