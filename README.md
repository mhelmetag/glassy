# glassy

Machine learning to predict clean and choppy surf conditions

# Setup

Requirements:

- ffmpeg
- pipenv
- python3

# Local

Testing can be done with these photos or others:

- glassy: https://i.ibb.co/xG78GSc/1574353614-5842041f4e65fad6a7708966-0019.jpg
- choppy: https://i.ibb.co/f2MFGcQ/1574746546-20191125-T201826428-18.jpg

For instance, running a GET request for `http://localhost:8000/classify-url?url=https://i.ibb.co/xG78GSc/1574353614-5842041f4e65fad6a7708966-0019.jpg`.

# Deployment

Deployed to Heroku using Starlette and uvicorn.
