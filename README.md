# heroku-multiplex

Deploy multiple apps to single Heroku dyno using [Honcho](https://pypi.org/project/honcho/) and [Flask](https://palletsprojects.com/p/flask/).

1. Add [run scripts](https://honcho.readthedocs.io/en/latest/#what-are-procfiles) to `ProcfileHoncho`. Each application can behave as its own root server so long as it's bound to a separate port.
1. Optionally, add an [environment file](https://honcho.readthedocs.io/en/latest/using_procfiles.html#environment-files) to setup source-controlled environment variables for port numbers.
1. Add application routing to the `modules` dictionary in `app.py`.
1. Start `honcho`.

   ```bash
   virtualenv -p python3 env
   source env/bin/activate
   pip install -r requirements.txt
   honcho start
   ```
