# Blog1

Blog made using Flask

## Installation

1. Clone this repository: `git clone https://github.com/natharyan/Blog1.git`
2. (optional) Activate a [Virtual Environment](https://startbootstrap.com/theme/clean-blog): `python3 -m venv “__virtualenv_name__”`
3. run: `pip install -r requirements.txt` in your shell

## Usage

1. import [posts.sql](posts.sql) into your sql server
2. change ***"upload_location"*** in [config.json](config.json) to your [static](static) path
3. run `FLASK_APP=main.py`
4. run `FLASK_DEBUG=True` (optional)
5. run `flask run`
* Admin Panel Access: `127.0.0.1:(localhost_branch)/dashboard`
* Gmail: feel free to use the gmail account provided in config.json or add your own account (Resource: [Create & use App Passwords](https://support.google.com/mail/answer/185833?hl=en))

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## Credits

Design reference: [Clean Blog](https://startbootstrap.com/theme/clean-blog)